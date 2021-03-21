namespace CompGraph_Palitra
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.colorDialog1 = new System.Windows.Forms.ColorDialog();
            this.panel1 = new System.Windows.Forms.Panel();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.radioButton_RGB = new System.Windows.Forms.RadioButton();
            this.buttonOkColor = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.numericUpDown_A = new System.Windows.Forms.NumericUpDown();
            this.radioButton_CMYK = new System.Windows.Forms.RadioButton();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.textBox_C = new System.Windows.Forms.TextBox();
            this.textBox_M = new System.Windows.Forms.TextBox();
            this.textBox_Y = new System.Windows.Forms.TextBox();
            this.textBox_K = new System.Windows.Forms.TextBox();
            this.textBox_B = new System.Windows.Forms.TextBox();
            this.textBox_G = new System.Windows.Forms.TextBox();
            this.textBox_R = new System.Windows.Forms.TextBox();
            this.textBox_V = new System.Windows.Forms.TextBox();
            this.textBox_S = new System.Windows.Forms.TextBox();
            this.textBox_H = new System.Windows.Forms.TextBox();
            this.radioButton_HSV = new System.Windows.Forms.RadioButton();
            this.label9 = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.label11 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_A)).BeginInit();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.SystemColors.ActiveBorder;
            this.panel1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.panel1.Location = new System.Drawing.Point(450, 12);
            this.panel1.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(316, 310);
            this.panel1.TabIndex = 0;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(83, 35);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(21, 20);
            this.label1.TabIndex = 4;
            this.label1.Text = "R";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(145, 35);
            this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(22, 20);
            this.label2.TabIndex = 5;
            this.label2.Text = "G";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(210, 35);
            this.label3.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(20, 20);
            this.label3.TabIndex = 6;
            this.label3.Text = "B";
            // 
            // radioButton_RGB
            // 
            this.radioButton_RGB.AutoSize = true;
            this.radioButton_RGB.Checked = true;
            this.radioButton_RGB.Location = new System.Drawing.Point(278, 59);
            this.radioButton_RGB.Name = "radioButton_RGB";
            this.radioButton_RGB.Size = new System.Drawing.Size(63, 24);
            this.radioButton_RGB.TabIndex = 7;
            this.radioButton_RGB.Text = "RGB";
            this.radioButton_RGB.UseVisualStyleBackColor = true;
            this.radioButton_RGB.CheckedChanged += new System.EventHandler(this.radioButton_RGB_CheckedChanged);
            // 
            // buttonOkColor
            // 
            this.buttonOkColor.Location = new System.Drawing.Point(356, 12);
            this.buttonOkColor.Name = "buttonOkColor";
            this.buttonOkColor.Size = new System.Drawing.Size(87, 312);
            this.buttonOkColor.TabIndex = 8;
            this.buttonOkColor.Text = "Выбрать цвет";
            this.buttonOkColor.UseVisualStyleBackColor = true;
            this.buttonOkColor.Click += new System.EventHandler(this.buttonOkColor_Click);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(8, 32);
            this.label4.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(20, 20);
            this.label4.TabIndex = 10;
            this.label4.Text = "A";
            // 
            // numericUpDown_A
            // 
            this.numericUpDown_A.Location = new System.Drawing.Point(12, 57);
            this.numericUpDown_A.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.numericUpDown_A.Maximum = new decimal(new int[] {
            255,
            0,
            0,
            0});
            this.numericUpDown_A.Name = "numericUpDown_A";
            this.numericUpDown_A.Size = new System.Drawing.Size(56, 26);
            this.numericUpDown_A.TabIndex = 9;
            this.numericUpDown_A.Value = new decimal(new int[] {
            255,
            0,
            0,
            0});
            // 
            // radioButton_CMYK
            // 
            this.radioButton_CMYK.AutoSize = true;
            this.radioButton_CMYK.Location = new System.Drawing.Point(278, 148);
            this.radioButton_CMYK.Name = "radioButton_CMYK";
            this.radioButton_CMYK.Size = new System.Drawing.Size(72, 24);
            this.radioButton_CMYK.TabIndex = 17;
            this.radioButton_CMYK.Text = "CMYK";
            this.radioButton_CMYK.UseVisualStyleBackColor = true;
            this.radioButton_CMYK.CheckedChanged += new System.EventHandler(this.radioButton_CMYK_CheckedChanged);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(211, 125);
            this.label5.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(19, 20);
            this.label5.TabIndex = 16;
            this.label5.Text = "K";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(146, 125);
            this.label6.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(20, 20);
            this.label6.TabIndex = 15;
            this.label6.Text = "Y";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(84, 125);
            this.label7.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(22, 20);
            this.label7.TabIndex = 14;
            this.label7.Text = "M";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(20, 124);
            this.label8.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(20, 20);
            this.label8.TabIndex = 19;
            this.label8.Text = "C";
            // 
            // textBox_C
            // 
            this.textBox_C.Location = new System.Drawing.Point(24, 147);
            this.textBox_C.Name = "textBox_C";
            this.textBox_C.Size = new System.Drawing.Size(56, 26);
            this.textBox_C.TabIndex = 23;
            // 
            // textBox_M
            // 
            this.textBox_M.Location = new System.Drawing.Point(86, 147);
            this.textBox_M.Name = "textBox_M";
            this.textBox_M.Size = new System.Drawing.Size(56, 26);
            this.textBox_M.TabIndex = 24;
            // 
            // textBox_Y
            // 
            this.textBox_Y.Location = new System.Drawing.Point(152, 148);
            this.textBox_Y.Name = "textBox_Y";
            this.textBox_Y.Size = new System.Drawing.Size(56, 26);
            this.textBox_Y.TabIndex = 25;
            // 
            // textBox_K
            // 
            this.textBox_K.Location = new System.Drawing.Point(214, 148);
            this.textBox_K.Name = "textBox_K";
            this.textBox_K.Size = new System.Drawing.Size(56, 26);
            this.textBox_K.TabIndex = 26;
            // 
            // textBox_B
            // 
            this.textBox_B.Location = new System.Drawing.Point(214, 59);
            this.textBox_B.Name = "textBox_B";
            this.textBox_B.Size = new System.Drawing.Size(56, 26);
            this.textBox_B.TabIndex = 29;
            this.textBox_B.Text = "81";
            // 
            // textBox_G
            // 
            this.textBox_G.Location = new System.Drawing.Point(152, 59);
            this.textBox_G.Name = "textBox_G";
            this.textBox_G.Size = new System.Drawing.Size(56, 26);
            this.textBox_G.TabIndex = 28;
            this.textBox_G.Text = "214";
            // 
            // textBox_R
            // 
            this.textBox_R.Location = new System.Drawing.Point(86, 58);
            this.textBox_R.Name = "textBox_R";
            this.textBox_R.Size = new System.Drawing.Size(56, 26);
            this.textBox_R.TabIndex = 27;
            this.textBox_R.Text = "255";
            // 
            // textBox_V
            // 
            this.textBox_V.Location = new System.Drawing.Point(214, 240);
            this.textBox_V.Name = "textBox_V";
            this.textBox_V.Size = new System.Drawing.Size(56, 26);
            this.textBox_V.TabIndex = 36;
            // 
            // textBox_S
            // 
            this.textBox_S.Location = new System.Drawing.Point(152, 240);
            this.textBox_S.Name = "textBox_S";
            this.textBox_S.Size = new System.Drawing.Size(56, 26);
            this.textBox_S.TabIndex = 35;
            // 
            // textBox_H
            // 
            this.textBox_H.Location = new System.Drawing.Point(86, 239);
            this.textBox_H.Name = "textBox_H";
            this.textBox_H.Size = new System.Drawing.Size(56, 26);
            this.textBox_H.TabIndex = 34;
            // 
            // radioButton_HSV
            // 
            this.radioButton_HSV.AutoSize = true;
            this.radioButton_HSV.Location = new System.Drawing.Point(278, 240);
            this.radioButton_HSV.Name = "radioButton_HSV";
            this.radioButton_HSV.Size = new System.Drawing.Size(61, 24);
            this.radioButton_HSV.TabIndex = 33;
            this.radioButton_HSV.Text = "HSV";
            this.radioButton_HSV.UseVisualStyleBackColor = true;
            this.radioButton_HSV.CheckedChanged += new System.EventHandler(this.radioButton_HSV_CheckedChanged);
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(210, 216);
            this.label9.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(20, 20);
            this.label9.TabIndex = 32;
            this.label9.Text = "V";
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(145, 216);
            this.label10.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(20, 20);
            this.label10.TabIndex = 31;
            this.label10.Text = "S";
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Location = new System.Drawing.Point(83, 216);
            this.label11.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(21, 20);
            this.label11.TabIndex = 30;
            this.label11.Text = "H";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(774, 336);
            this.Controls.Add(this.textBox_V);
            this.Controls.Add(this.textBox_S);
            this.Controls.Add(this.textBox_H);
            this.Controls.Add(this.radioButton_HSV);
            this.Controls.Add(this.label9);
            this.Controls.Add(this.label10);
            this.Controls.Add(this.label11);
            this.Controls.Add(this.textBox_B);
            this.Controls.Add(this.textBox_G);
            this.Controls.Add(this.textBox_R);
            this.Controls.Add(this.textBox_K);
            this.Controls.Add(this.textBox_Y);
            this.Controls.Add(this.textBox_M);
            this.Controls.Add(this.textBox_C);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.radioButton_CMYK);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.numericUpDown_A);
            this.Controls.Add(this.buttonOkColor);
            this.Controls.Add(this.radioButton_RGB);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.panel1);
            this.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_A)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ColorDialog colorDialog1;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.RadioButton radioButton_RGB;
        private System.Windows.Forms.Button buttonOkColor;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.NumericUpDown numericUpDown_A;
        private System.Windows.Forms.RadioButton radioButton_CMYK;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.TextBox textBox_C;
        private System.Windows.Forms.TextBox textBox_M;
        private System.Windows.Forms.TextBox textBox_Y;
        private System.Windows.Forms.TextBox textBox_K;
        private System.Windows.Forms.TextBox textBox_B;
        private System.Windows.Forms.TextBox textBox_G;
        private System.Windows.Forms.TextBox textBox_R;
        private System.Windows.Forms.TextBox textBox_V;
        private System.Windows.Forms.TextBox textBox_S;
        private System.Windows.Forms.TextBox textBox_H;
        private System.Windows.Forms.RadioButton radioButton_HSV;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label label11;
    }
}

