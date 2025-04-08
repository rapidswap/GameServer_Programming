namespace DummyClient
{
    partial class CreateCharacter
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
            CreateButton = new Button();
            BackButton = new Button();
            Id_Text = new TextBox();
            Pw_Text = new TextBox();
            Oid_Text = new TextBox();
            Name_Text = new TextBox();
            Lv_Text = new TextBox();
            Exp_Text = new TextBox();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            label5 = new Label();
            label6 = new Label();
            SuspendLayout();
            // 
            // CreateButton
            // 
            CreateButton.Location = new Point(107, 311);
            CreateButton.Name = "CreateButton";
            CreateButton.Size = new Size(75, 23);
            CreateButton.TabIndex = 0;
            CreateButton.Text = "회원가입";
            CreateButton.UseVisualStyleBackColor = true;
            CreateButton.Click += Create_click;
            // 
            // BackButton
            // 
            BackButton.Location = new Point(203, 311);
            BackButton.Name = "BackButton";
            BackButton.Size = new Size(75, 23);
            BackButton.TabIndex = 1;
            BackButton.Text = "뒤로가기";
            BackButton.UseVisualStyleBackColor = true;
            BackButton.Click += Back_click;
            // 
            // Id_Text
            // 
            Id_Text.Location = new Point(152, 42);
            Id_Text.Name = "Id_Text";
            Id_Text.Size = new Size(100, 23);
            Id_Text.TabIndex = 2;
            // 
            // Pw_Text
            // 
            Pw_Text.Location = new Point(152, 84);
            Pw_Text.Name = "Pw_Text";
            Pw_Text.Size = new Size(100, 23);
            Pw_Text.TabIndex = 3;
            //
            //// Oid_Text
            // 
            Oid_Text.Location = new Point(152, 127);
            Oid_Text.Name = "Oid_Text";
            Oid_Text.Size = new Size(100, 23);
            Oid_Text.TabIndex = 4;
            // 
            // Name_Text
            // 
            Name_Text.Location = new Point(152, 171);
            Name_Text.Name = "Name_Text";
            Name_Text.Size = new Size(100, 23);
            Name_Text.TabIndex = 5;
            // 
            // Lv_Text
            // 
            Lv_Text.Location = new Point(152, 215);
            Lv_Text.Name = "Lv_Text";
            Lv_Text.Size = new Size(100, 23);
            Lv_Text.TabIndex = 6;
            // 
            // Exp_Text
            // 
            Exp_Text.Location = new Point(152, 260);
            Exp_Text.Name = "Exp_Text";
            Exp_Text.Size = new Size(100, 23);
            Exp_Text.TabIndex = 7;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(127, 45);
            label1.Name = "label1";
            label1.Size = new Size(19, 15);
            label1.TabIndex = 8;
            label1.Text = "ID";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(121, 92);
            label2.Name = "label2";
            label2.Size = new Size(25, 15);
            label2.TabIndex = 9;
            label2.Text = "PW";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(118, 130);
            label3.Name = "label3";
            label3.Size = new Size(28, 15);
            label3.TabIndex = 10;
            label3.Text = "OID";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(107, 174);
            label4.Name = "label4";
            label4.Size = new Size(39, 15);
            label4.TabIndex = 11;
            label4.Text = "Name";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(112, 218);
            label5.Name = "label5";
            label5.Size = new Size(34, 15);
            label5.TabIndex = 12;
            label5.Text = "Level";
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Location = new Point(119, 263);
            label6.Name = "label6";
            label6.Size = new Size(27, 15);
            label6.TabIndex = 13;
            label6.Text = "EXP";
            // 
            // CreateCharacter
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(label6);
            Controls.Add(label5);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(Exp_Text);
            Controls.Add(Lv_Text);
            Controls.Add(Name_Text);
            Controls.Add(Oid_Text);
            Controls.Add(Pw_Text);
            Controls.Add(Id_Text);
            Controls.Add(BackButton);
            Controls.Add(CreateButton);
            Name = "CreateCharacter";
            Text = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button CreateButton;
        private Button BackButton;
        private TextBox Id_Text;
        private TextBox Pw_Text;
        private TextBox Oid_Text;
        private TextBox Name_Text;
        private TextBox Lv_Text;
        private TextBox Exp_Text;
        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
        private Label label5;
        private Label label6;
    }
}