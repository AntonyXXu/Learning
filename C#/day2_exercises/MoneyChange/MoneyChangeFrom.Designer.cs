
namespace MoneyChange
{
    partial class MoneyChangeFrom
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MoneyChangeFrom));
            this.label1 = new System.Windows.Forms.Label();
            this.MoneyIn = new System.Windows.Forms.TextBox();
            this.CalcChange = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.ToonieSh = new System.Windows.Forms.Label();
            this.InPenny = new System.Windows.Forms.RadioButton();
            this.NoPenny = new System.Windows.Forms.RadioButton();
            this.GBoxPenny = new System.Windows.Forms.GroupBox();
            this.label3 = new System.Windows.Forms.Label();
            this.PennySh = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.LoonieSh = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.QuarterSh = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.DimeSh = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.NickelSh = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.label7 = new System.Windows.Forms.Label();
            this.GBoxPenny.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(42, 35);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(110, 20);
            this.label1.TabIndex = 0;
            this.label1.Text = "Money ($ CAD)";
            // 
            // MoneyIn
            // 
            this.MoneyIn.Location = new System.Drawing.Point(212, 32);
            this.MoneyIn.Name = "MoneyIn";
            this.MoneyIn.Size = new System.Drawing.Size(141, 27);
            this.MoneyIn.TabIndex = 1;
            this.MoneyIn.TextChanged += new System.EventHandler(this.MoneyIn_TextChanged);
            // 
            // CalcChange
            // 
            this.CalcChange.BackColor = System.Drawing.Color.DeepSkyBlue;
            this.CalcChange.FlatAppearance.BorderColor = System.Drawing.Color.Lime;
            this.CalcChange.FlatAppearance.MouseDownBackColor = System.Drawing.Color.Aqua;
            this.CalcChange.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(192)))), ((int)(((byte)(192)))));
            this.CalcChange.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.CalcChange.ForeColor = System.Drawing.SystemColors.ControlText;
            this.CalcChange.Location = new System.Drawing.Point(212, 81);
            this.CalcChange.Name = "CalcChange";
            this.CalcChange.Size = new System.Drawing.Size(141, 38);
            this.CalcChange.TabIndex = 2;
            this.CalcChange.Text = "Calculate Change";
            this.CalcChange.UseVisualStyleBackColor = false;
            this.CalcChange.Click += new System.EventHandler(this.CalcChange_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(74, 351);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(54, 20);
            this.label2.TabIndex = 3;
            this.label2.Text = "Toonie";
            // 
            // ToonieSh
            // 
            this.ToonieSh.AutoSize = true;
            this.ToonieSh.ForeColor = System.Drawing.Color.Blue;
            this.ToonieSh.Location = new System.Drawing.Point(261, 35);
            this.ToonieSh.Name = "ToonieSh";
            this.ToonieSh.Size = new System.Drawing.Size(0, 20);
            this.ToonieSh.TabIndex = 4;
            // 
            // InPenny
            // 
            this.InPenny.AutoSize = true;
            this.InPenny.Location = new System.Drawing.Point(32, 26);
            this.InPenny.Name = "InPenny";
            this.InPenny.Size = new System.Drawing.Size(120, 24);
            this.InPenny.TabIndex = 5;
            this.InPenny.Text = "Include Penny";
            this.InPenny.UseVisualStyleBackColor = true;
            this.InPenny.CheckedChanged += new System.EventHandler(this.radioButton1_CheckedChanged);
            // 
            // NoPenny
            // 
            this.NoPenny.AutoSize = true;
            this.NoPenny.Location = new System.Drawing.Point(261, 26);
            this.NoPenny.Name = "NoPenny";
            this.NoPenny.Size = new System.Drawing.Size(92, 24);
            this.NoPenny.TabIndex = 6;
            this.NoPenny.Text = "No Penny";
            this.NoPenny.UseVisualStyleBackColor = true;
            this.NoPenny.CheckedChanged += new System.EventHandler(this.radioButton2_CheckedChanged);
            // 
            // GBoxPenny
            // 
            this.GBoxPenny.Controls.Add(this.NoPenny);
            this.GBoxPenny.Controls.Add(this.InPenny);
            this.GBoxPenny.Location = new System.Drawing.Point(42, 75);
            this.GBoxPenny.Name = "GBoxPenny";
            this.GBoxPenny.Size = new System.Drawing.Size(420, 71);
            this.GBoxPenny.TabIndex = 7;
            this.GBoxPenny.TabStop = false;
            this.GBoxPenny.Text = "Penny";
            this.GBoxPenny.Enter += new System.EventHandler(this.groupBox1_Enter);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(32, 303);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(47, 20);
            this.label3.TabIndex = 8;
            this.label3.Text = "Penny";
            // 
            // PennySh
            // 
            this.PennySh.AutoSize = true;
            this.PennySh.ForeColor = System.Drawing.Color.Blue;
            this.PennySh.Location = new System.Drawing.Point(261, 303);
            this.PennySh.Name = "PennySh";
            this.PennySh.Size = new System.Drawing.Size(0, 20);
            this.PennySh.TabIndex = 9;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(74, 403);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(54, 20);
            this.label4.TabIndex = 10;
            this.label4.Text = "Loonie";
            // 
            // LoonieSh
            // 
            this.LoonieSh.AutoSize = true;
            this.LoonieSh.ForeColor = System.Drawing.Color.Blue;
            this.LoonieSh.Location = new System.Drawing.Point(261, 87);
            this.LoonieSh.Name = "LoonieSh";
            this.LoonieSh.Size = new System.Drawing.Size(0, 20);
            this.LoonieSh.TabIndex = 11;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(74, 456);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(59, 20);
            this.label5.TabIndex = 12;
            this.label5.Text = "Quarter";
            // 
            // QuarterSh
            // 
            this.QuarterSh.AutoSize = true;
            this.QuarterSh.ForeColor = System.Drawing.Color.Blue;
            this.QuarterSh.Location = new System.Drawing.Point(303, 456);
            this.QuarterSh.Name = "QuarterSh";
            this.QuarterSh.Size = new System.Drawing.Size(0, 20);
            this.QuarterSh.TabIndex = 13;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(74, 510);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(45, 20);
            this.label6.TabIndex = 14;
            this.label6.Text = "Dime";
            // 
            // DimeSh
            // 
            this.DimeSh.AutoSize = true;
            this.DimeSh.ForeColor = System.Drawing.Color.Blue;
            this.DimeSh.Location = new System.Drawing.Point(303, 510);
            this.DimeSh.Name = "DimeSh";
            this.DimeSh.Size = new System.Drawing.Size(0, 20);
            this.DimeSh.TabIndex = 15;
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(74, 566);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(50, 20);
            this.label8.TabIndex = 16;
            this.label8.Text = "Nickel";
            // 
            // NickelSh
            // 
            this.NickelSh.AutoSize = true;
            this.NickelSh.ForeColor = System.Drawing.Color.Blue;
            this.NickelSh.Location = new System.Drawing.Point(303, 566);
            this.NickelSh.Name = "NickelSh";
            this.NickelSh.Size = new System.Drawing.Size(0, 20);
            this.NickelSh.TabIndex = 17;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.CalcChange);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.MoneyIn);
            this.groupBox1.Location = new System.Drawing.Point(42, 170);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(420, 128);
            this.groupBox1.TabIndex = 18;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Input";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.PennySh);
            this.groupBox2.Controls.Add(this.label3);
            this.groupBox2.Controls.Add(this.LoonieSh);
            this.groupBox2.Controls.Add(this.ToonieSh);
            this.groupBox2.Location = new System.Drawing.Point(42, 316);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(420, 360);
            this.groupBox2.TabIndex = 19;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Output - Change";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(42, 19);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(419, 20);
            this.label7.TabIndex = 20;
            this.label7.Text = "Ehsan Jalali              Assignment 1, Part 2              Apr.19, 2021  ";
            this.label7.Click += new System.EventHandler(this.label7_Click);
            // 
            // MoneyChangeFrom
            // 
            this.AcceptButton = this.CalcChange;
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(510, 714);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.NickelSh);
            this.Controls.Add(this.label8);
            this.Controls.Add(this.DimeSh);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.QuarterSh);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.GBoxPenny);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.groupBox2);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "MoneyChangeFrom";
            this.Text = "Money Change";
            this.Load += new System.EventHandler(this.MoneyChangeFrom_Load);
            this.GBoxPenny.ResumeLayout(false);
            this.GBoxPenny.PerformLayout();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox MoneyIn;
        private System.Windows.Forms.Button CalcChange;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label ToonieSh;
        private System.Windows.Forms.RadioButton InPenny;
        private System.Windows.Forms.RadioButton NoPenny;
        private System.Windows.Forms.GroupBox GBoxPenny;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label PennySh;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label LoonieSh;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label QuarterSh;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label DimeSh;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label NickelSh;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Label label7;
    }
}

