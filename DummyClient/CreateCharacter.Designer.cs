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
            Name_Text = new TextBox();
            label1 = new Label();
            label2 = new Label();
            label4 = new Label();
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
            // Name_Text
            // 
            Name_Text.Location = new Point(152, 129);
            Name_Text.Name = "Name_Text";
            Name_Text.Size = new Size(100, 23);
            Name_Text.TabIndex = 5;
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
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(107, 132);
            label4.Name = "label4";
            label4.Size = new Size(39, 15);
            label4.TabIndex = 11;
            label4.Text = "Name";
            // 
            // CreateCharacter
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(label4);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(Name_Text);
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
        private TextBox Name_Text;
        private Label label1;
        private Label label2;
        private Label label4;
    }
}