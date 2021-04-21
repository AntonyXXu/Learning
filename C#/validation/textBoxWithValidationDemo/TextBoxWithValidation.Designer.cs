namespace textBoxWithValidationDemo
{
    partial class TextBoxWithValidation
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.integerInputTextbox = new System.Windows.Forms.TextBox();
            this.integerInputStatusLabel = new System.Windows.Forms.Label();
            this.processIntegerButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // integerInputTextbox
            // 
            this.integerInputTextbox.Location = new System.Drawing.Point(24, 13);
            this.integerInputTextbox.Name = "integerInputTextbox";
            this.integerInputTextbox.Size = new System.Drawing.Size(100, 20);
            this.integerInputTextbox.TabIndex = 0;
            this.integerInputTextbox.TextChanged += new System.EventHandler(this.IntegerInputTextbox_TextChanged);
            // 
            // integerInputStatusLabel
            // 
            this.integerInputStatusLabel.AutoSize = true;
            this.integerInputStatusLabel.Location = new System.Drawing.Point(141, 13);
            this.integerInputStatusLabel.Name = "integerInputStatusLabel";
            this.integerInputStatusLabel.Size = new System.Drawing.Size(29, 13);
            this.integerInputStatusLabel.TabIndex = 1;
            this.integerInputStatusLabel.Text = "BAD";
            // 
            // processIntegerButton
            // 
            this.processIntegerButton.Enabled = false;
            this.processIntegerButton.Location = new System.Drawing.Point(144, 44);
            this.processIntegerButton.Name = "processIntegerButton";
            this.processIntegerButton.Size = new System.Drawing.Size(75, 23);
            this.processIntegerButton.TabIndex = 2;
            this.processIntegerButton.Text = "Process";
            this.processIntegerButton.UseVisualStyleBackColor = true;
            // 
            // TextBoxWithValidation
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(288, 84);
            this.Controls.Add(this.processIntegerButton);
            this.Controls.Add(this.integerInputStatusLabel);
            this.Controls.Add(this.integerInputTextbox);
            this.Name = "TextBoxWithValidation";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Textbox with Validation Demo";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox integerInputTextbox;
        private System.Windows.Forms.Label integerInputStatusLabel;
        private System.Windows.Forms.Button processIntegerButton;
    }
}

