namespace DummyClient
{
    partial class DummyClient
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
            mainPanel_ = new Panel();
            SuspendLayout();
            // 
            // mainPanel_
            // 
            mainPanel_.Location = new Point(0, 0);
            mainPanel_.Name = "mainPanel_";
            mainPanel_.Size = new Size(800, 489);
            mainPanel_.TabIndex = 0;
            // 
            // DummyClient
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(782, 450);
            Controls.Add(mainPanel_);
            FormBorderStyle = FormBorderStyle.FixedToolWindow;
            Name = "DummyClient";
            Text = "DummyClient";
            Load += Form1_Load;
            ResumeLayout(false);
        }

        #endregion

        public Panel mainPanel_;
    }
}
