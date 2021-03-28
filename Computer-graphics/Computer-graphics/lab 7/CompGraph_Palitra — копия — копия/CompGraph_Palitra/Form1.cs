using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


// cmyk from 0 to 100
// rgb from 0 to 255
// hsv 239 240 240
namespace CompGraph_Palitra
{
    public partial class Form1 : Form
    {
        public int[] RGB = new int[] { 0, 0, 0 };
        public float[] CMYK = new float[] { 0, 0, 0, 0 };
        public float[] HSV = new float[] { 0, 0, 0 };
        public int Alpha = 0;

        public Form1()
        {
            InitializeComponent();          
        }

        private void Form1_Load(object sender, EventArgs e)
        {            
            radioButton_CMYK.Checked = true; radioButton_CMYK.Checked = false;
            radioButton_HSV.Checked = true; radioButton_HSV.Checked = false;
            radioButton_RGB.Checked = true;
        }

        private void buttonOkColor_Click(object sender, EventArgs e)
        {
            Alpha = Convert.ToInt32(numericUpDown_A.Value);
            if (radioButton_RGB.Checked == true)
            {
                GetRGBfromTextBox();
                FromRGBtoCMYK(RGB[0], RGB[1], RGB[2]);
                FromRGBtoHSV(RGB[0], RGB[1], RGB[2]);
                UpdateTextBoxAndColor();
            }
            else
            if (radioButton_CMYK.Checked == true)
            {
                GetCMYKfromTextBox();
                FromCMYKtoRGB(CMYK[0], CMYK[1], CMYK[2], CMYK[3]);
                FromRGBtoHSV(RGB[0], RGB[1], RGB[2]);
                UpdateTextBoxAndColor();
            }
            else
            if(radioButton_HSV.Checked == true)
            {
                GetHSVfromTextBox();
                Color color = FromHSVtoRGB_part1(HSV[0], HSV[1], HSV[2]);
                RGB[0] = color.R;
                RGB[1] = color.G;
                RGB[2] = color.B;
                FromRGBtoCMYK(RGB[0], RGB[1], RGB[2]);
                UpdateTextBoxAndColor();
            }
        }

        public void GetRGBfromTextBox()
        {
            RGB[0] = Convert.ToInt32(textBox_R.Text);
            RGB[1] = Convert.ToInt32(textBox_G.Text);
            RGB[2] = Convert.ToInt32(textBox_B.Text);
        }

        public void GetCMYKfromTextBox()
        {
            CMYK[0] = float.Parse(textBox_C.Text);
            CMYK[1] = float.Parse(textBox_M.Text);
            CMYK[2] = float.Parse(textBox_Y.Text);
            CMYK[3] = float.Parse(textBox_K.Text);
        }

        public void GetHSVfromTextBox()
        {
            HSV[0] = float.Parse(textBox_H.Text);
            HSV[1] = float.Parse(textBox_S.Text);
            HSV[2] = float.Parse(textBox_V.Text);
        }

        public void UpdateTextBoxAndColor()
        {
            textBox_R.Text = RGB[0].ToString();
            textBox_G.Text = RGB[1].ToString();
            textBox_B.Text = RGB[2].ToString();

            textBox_C.Text = Math.Round(CMYK[0], 2).ToString();
            textBox_M.Text = Math.Round(CMYK[1], 2).ToString();
            textBox_Y.Text = Math.Round(CMYK[2], 2).ToString();
            textBox_K.Text = Math.Round(CMYK[3], 2).ToString();

            textBox_H.Text = Math.Round(HSV[0], 2).ToString();
            textBox_S.Text = Math.Round(HSV[1], 2).ToString();
            textBox_V.Text = Math.Round(HSV[2], 2).ToString();

            panel1.BackColor = Color.FromArgb(Alpha, RGB[0], RGB[1], RGB[2]);
        }

        public void FromRGBtoCMYK(int R, int G, int B)
        {
            float rf, gf, bf;
            rf = R; rf /= 255;
            gf = G; gf /= 255;
            bf = B; bf /= 255;

            CMYK[3] = 1 - Math.Max(rf, Math.Max(bf, gf));
            CMYK[0] = (1 - rf - CMYK[3]) / (1 - CMYK[3]);
            CMYK[1] = (1 - gf - CMYK[3]) / (1 - CMYK[3]);
            CMYK[2] = (1 - bf - CMYK[3]) / (1 - CMYK[3]);
        }

        public void FromCMYKtoRGB(float C, float M, float Y, float K)
        {
            RGB[0] = Convert.ToInt32(255 * (1 - CMYK[0]) * (1 - CMYK[3]));
            RGB[1] = Convert.ToInt32(255 * (1 - CMYK[1]) * (1 - CMYK[3]));
            RGB[2] = Convert.ToInt32(255 * (1 - CMYK[2]) * (1 - CMYK[3]));
        }

        public void FromRGBtoHSV(int R, int G, int B)
        {

            float rf, gf, bf;
            rf = R; rf /= 255;
            gf = G; gf /= 255;
            bf = B; bf /= 255;

            float var_Min = Math.Min(rf, Math.Min(bf, gf));
            float var_Max = Math.Max(rf, Math.Max(bf, gf));
            float del_Max = var_Max - var_Min;
            HSV[2] = var_Max; // * 100;

            if(del_Max==0)
            {
                HSV[0] = 0;
                HSV[1] = 0;
            }
            else
            {
                HSV[1] = (del_Max / var_Max); //* 100;

                float del_R = (((var_Max - rf) / 6) + (del_Max / 2)) / del_Max;
                float del_G = (((var_Max - gf) / 6) + (del_Max / 2)) / del_Max;
                float del_B = (((var_Max - bf) / 6) + (del_Max / 2)) / del_Max;

                if (rf == var_Max)
                {                  
                    HSV[0] = (60 * ((gf - bf) / del_Max) + 360) % 360;
                }
                else
                if(gf == var_Max)
                {                    
                    HSV[0] = (60 * ((bf - rf) / del_Max) + 120) % 360;
                }
                else
                if (bf == var_Max)
                {                  
                    HSV[0] = (60 * ((rf - gf) / del_Max) + 240) % 360;
                }
            }
        }

        public static Color FromHSVtoRGB_part1(float hue, float saturation, float value)
        {
            int hi = Convert.ToInt32(Math.Floor(hue / 60)) % 6;
            double f = hue / 60 - Math.Floor(hue / 60);


            value = value * 255;
            int v = Convert.ToInt32(value);
            int p = Convert.ToInt32(value * (1 - saturation));
            int q = Convert.ToInt32(value * (1 - f * saturation));
            int t = Convert.ToInt32(value * (1 - (1 - f) * saturation));

            if (hi == 0)
                return Color.FromArgb(255, v, t, p);
            else if (hi == 1)
                return Color.FromArgb(255, q, v, p);
            else if (hi == 2)
                return Color.FromArgb(255, p, v, t);
            else if (hi == 3)
                return Color.FromArgb(255, p, q, v);
            else if (hi == 4)
                return Color.FromArgb(255, t, p, v);
            else
                return Color.FromArgb(255, v, p, q);
        }

        private void radioButton_RGB_CheckedChanged(object sender, EventArgs e)
        {
            if(radioButton_RGB.Checked == false)
            {
                textBox_R.Enabled = false;
                textBox_G.Enabled = false;
                textBox_B.Enabled = false;               
            }
            else
            {
                textBox_R.Enabled = true;
                textBox_G.Enabled = true;
                textBox_B.Enabled = true;
            }
        }

        private void radioButton_CMYK_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton_CMYK.Checked == false)
            {
                textBox_C.Enabled = false;
                textBox_M.Enabled = false;
                textBox_Y.Enabled = false;
                textBox_K.Enabled = false;
            }
            else
            {
                textBox_C.Enabled = true;
                textBox_M.Enabled = true;
                textBox_Y.Enabled = true;
                textBox_K.Enabled = true;
            }
        }

        private void radioButton_HSV_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton_HSV.Checked == false)
            {
                textBox_H.Enabled = false;
                textBox_S.Enabled = false;
                textBox_V.Enabled = false;
            }
            else
            {
                textBox_H.Enabled = true;
                textBox_S.Enabled = true;
                textBox_V.Enabled = true;
            }
        }
    }
}
