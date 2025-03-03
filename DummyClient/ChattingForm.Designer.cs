namespace DummyClient
{
    partial class ChattingForm
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
            textBox_input_ = new TextBox();
            richTextBox_view_ = new RichTextBox();
            exitButton_ = new Button();
            SuspendLayout();
            // 
            // textBox_input_
            // 
            textBox_input_.Location = new Point(20, 392);
            textBox_input_.Margin = new Padding(3, 4, 3, 4);
            textBox_input_.Name = "textBox_input_";
            textBox_input_.Size = new Size(456, 23);
            textBox_input_.TabIndex = 3;
            textBox_input_.KeyDown += textBox_input_KeyDown;
            // 
            // richTextBox_view_
            // 
            richTextBox_view_.BackColor = Color.Teal;
            richTextBox_view_.ForeColor = Color.White;
            richTextBox_view_.Location = new Point(20, 15);
            richTextBox_view_.Margin = new Padding(3, 4, 3, 4);
            richTextBox_view_.Name = "richTextBox_view_";
            richTextBox_view_.ReadOnly = true;
            richTextBox_view_.ScrollBars = RichTextBoxScrollBars.Vertical;
            richTextBox_view_.Size = new Size(457, 369);
            richTextBox_view_.TabIndex = 2;
            richTextBox_view_.Text = "";
            // 
            // exitButton_
            // 
            exitButton_.Location = new Point(192, 439);
            exitButton_.Name = "exitButton_";
            exitButton_.Size = new Size(75, 23);
            exitButton_.TabIndex = 4;
            exitButton_.Text = "button1";
            exitButton_.UseVisualStyleBackColor = true;
            exitButton_.Click += leaveUsers;
            // 
            // ChattingForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            AutoSize = true;
            AutoSizeMode = AutoSizeMode.GrowAndShrink;
            ClientSize = new Size(498, 495);
            Controls.Add(exitButton_);
            Controls.Add(textBox_input_);
            Controls.Add(richTextBox_view_);
            FormBorderStyle = FormBorderStyle.None;
            Margin = new Padding(3, 4, 3, 4);
            Name = "ChattingForm";
            Text = "ChattingForm";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private System.Windows.Forms.TextBox textBox_input_;
        private System.Windows.Forms.RichTextBox richTextBox_view_;
        private Button exitButton_;
    }
}