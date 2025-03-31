namespace DummyClient
{
    partial class LoginForm
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
            textBox_id_ = new TextBox();
            textBox_pw_ = new TextBox();
            label1 = new Label();
            label2 = new Label();
            button_login_ = new Button();
            button_quit_ = new Button();
            button1 = new Button();
            SuspendLayout();
            // 
            // textBox_id_
            // 
            textBox_id_.Location = new Point(78, 31);
            textBox_id_.Margin = new Padding(3, 4, 3, 4);
            textBox_id_.Name = "textBox_id_";
            textBox_id_.Size = new Size(109, 23);
            textBox_id_.TabIndex = 0;
            // 
            // textBox_pw_
            // 
            textBox_pw_.Location = new Point(78, 65);
            textBox_pw_.Margin = new Padding(3, 4, 3, 4);
            textBox_pw_.Name = "textBox_pw_";
            textBox_pw_.PasswordChar = '*';
            textBox_pw_.Size = new Size(109, 23);
            textBox_pw_.TabIndex = 1;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(33, 35);
            label1.Name = "label1";
            label1.Size = new Size(19, 15);
            label1.TabIndex = 2;
            label1.Text = "ID";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(10, 69);
            label2.Name = "label2";
            label2.Size = new Size(57, 15);
            label2.TabIndex = 3;
            label2.Text = "Password";
            // 
            // button_login_
            // 
            button_login_.Location = new Point(12, 114);
            button_login_.Margin = new Padding(3, 4, 3, 4);
            button_login_.Name = "button_login_";
            button_login_.Size = new Size(75, 29);
            button_login_.TabIndex = 4;
            button_login_.Text = "로그인";
            button_login_.UseVisualStyleBackColor = true;
            button_login_.Click += button_login_Click;
            // 
            // button_quit_
            // 
            button_quit_.Location = new Point(107, 115);
            button_quit_.Margin = new Padding(3, 4, 3, 4);
            button_quit_.Name = "button_quit_";
            button_quit_.Size = new Size(75, 29);
            button_quit_.TabIndex = 5;
            button_quit_.Text = "종료";
            button_quit_.UseVisualStyleBackColor = true;
            button_quit_.Click += button_quit;
            // 
            // button1
            // 
            button1.Location = new Point(201, 113);
            button1.Name = "button1";
            button1.Size = new Size(75, 30);
            button1.TabIndex = 6;
            button1.Text = "캐릭터생성";
            button1.UseVisualStyleBackColor = true;
            button1.Click += Character_Click;
            // 
            // LoginForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            AutoSize = true;
            AutoSizeMode = AutoSizeMode.GrowAndShrink;
            ClientSize = new Size(288, 175);
            Controls.Add(button1);
            Controls.Add(button_quit_);
            Controls.Add(button_login_);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(textBox_pw_);
            Controls.Add(textBox_id_);
            FormBorderStyle = FormBorderStyle.None;
            Margin = new Padding(3, 4, 3, 4);
            Name = "LoginForm";
            Text = "DummyLogin";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private System.Windows.Forms.TextBox textBox_id_;
        private System.Windows.Forms.TextBox textBox_pw_;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button button_login_;
        private System.Windows.Forms.Button button_quit_;
        private Button button1;
    }
}