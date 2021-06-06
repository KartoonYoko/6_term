using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


// http://wladm.narod.ru/C_Sharp/flame01.html

namespace laba_19
{
    public partial class Form1 : Form
    {
        //Рабочий рисунок
        private Bitmap workBmp = null;
        private Random rnd = new Random(DateTime.Now.Millisecond);
        private int viWidth = 320;
        private int viHeight = 180;
        //private int viWidth = 100;
        //private int viHeight = 180;
        public Form1()
        {
            InitializeComponent();
        }

       
        private void Form1_Load(object sender, EventArgs e)
        {
                vStartFlame();
        }


            #region vStartFlame() 
            private void vStartFlame()
            {
                workBmp = new Bitmap(viWidth, viHeight, PixelFormat.Format8bppIndexed);
                ColorPalette pal = workBmp.Palette;
                for (int i = 0; i < 64; i++)
                {
                    pal.Entries[i] = Color.FromArgb(i << 2, 0, 0);
                    pal.Entries[i + 64] = Color.FromArgb(255, i << 2, 0);
                    pal.Entries[i + 128] = Color.FromArgb(255, 255, i << 2);
                    //Попытка увеличить белую составляющую
                    pal.Entries[i + 192] = Color.FromArgb(255, 255, 255);
                }
                workBmp.Palette = pal;
            }
        #endregion




        private void timer1_Tick(object sender, EventArgs e)
        {
            //Прямая работа с памятью - не забудем в свойствах проекта на 
            //закладке Build поставить галочку Allow unsafe code.
            unsafe
            {
                BitmapData bmpLook = workBmp.LockBits(
                  new Rectangle(Point.Empty, workBmp.Size),
                  ImageLockMode.ReadWrite, PixelFormat.Format8bppIndexed);
                //bufdata - указатель на левую верхнюю точку рисунка
                Byte* pointtop = (Byte*)bmpLook.Scan0;
                //pointbottom - указатель на точку начала нижней линии рисунка
                Byte* pointbottom = pointtop + ((viHeight - 1) * viWidth);
                Byte* i = null;
                int j = 0;
                //Заполняем нижнюю линию точками, со случайно выбранными цветами
                //for (int x = 0; x < viWidth; x++)
                //{
                //    *(pointbottom + x) = (Byte)rnd.Next(0, 255);
                //}
                for (int x = viWidth / 3; x < viWidth - viWidth / 3; x++)
                {
                    *(pointbottom + x) = (Byte)rnd.Next(100, 255);
                }
                for (i = pointtop; i < pointbottom; i++)
                {
                    if (i > pointtop + 2 && i < pointbottom - 2)
                    {
                        j = *(i - 1) + *(i - 2) + *(i + 1) + *(i + 2) +
                                 *(i + viWidth) * 5;
                        j /= 9;
                        if (j < 0) j = 0;
                        *i = (Byte)j;
                    }
                }
                //Заполняем остальные точки, значениями усредненными по алгоритму
                //for (i = pointtop; i < pointbottom; i++)
                //{
                //    if (i != pointtop)
                //    {
                //        //Вес точки снизу увеличен до 3х
                //        j = *(i - 1) + *(i + 1) + *(i + viWidth) * 3;
                //        //Усредняем
                //        j /= 5;
                //        if (j < 0) j = 0;
                //        *i = (Byte)j;
                //    }
                //}
            
            //Разблокируем память
            workBmp.UnlockBits(bmpLook);
            bmpLook = null;
            //Два вспомогательных Bitmap для переноса изображения 
            //в PictureBox и для удаления ~ 4 pix из нижней части
            //Убирает нежелательный мусор при растяжении рисунка в 
            //PictureBox
            Bitmap bmpA = new Bitmap(viWidth, viHeight);
            bmpA = workBmp;
            Bitmap bmpB = new Bitmap(viWidth, viHeight - 4);
            Graphics grtmpB = Graphics.FromImage(bmpB);
            grtmpB.DrawImage(bmpA, 0, 0);
            grtmpB.Dispose();
            pictureBox1.Image = bmpB;
            bmpB = null;
            bmpA = null;
        }
        }



    }
    
}

