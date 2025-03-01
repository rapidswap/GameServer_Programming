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
            button_quit_ = new Button();
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
            // button_quit_
            // 
            button_quit_.Location = new Point(197, 453);
            button_quit_.Margin = new Padding(3, 4, 3, 4);
            button_quit_.Name = "button_quit_";
            button_quit_.Size = new Size(75, 29);
            button_quit_.TabIndex = 6;
            button_quit_.Text = "종료";
            button_quit_.UseVisualStyleBackColor = true;
            button_quit_.Click += button1_Click;
            // 
            // ChattingForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            AutoSize = true;
            AutoSizeMode = AutoSizeMode.GrowAndShrink;
            ClientSize = new Size(498, 495);
            Controls.Add(button_quit_);
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
        private Button button_quit_;
    }
}