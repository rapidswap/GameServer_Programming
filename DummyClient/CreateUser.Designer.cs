namespace DummyClient
{
    partial class CreateUser
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
            button1 = new Button();
            button2 = new Button();
            ID_Create = new TextBox();
            PW_Create = new TextBox();
            ID = new Label();
            label2 = new Label();
            SuspendLayout();
            // 
            // button1
            // 
            button1.Location = new Point(46, 160);
            button1.Name = "button1";
            button1.Size = new Size(97, 23);
            button1.TabIndex = 0;
            button1.Text = "아이디 생성";
            button1.UseVisualStyleBackColor = true;
            button1.Click += Create_Click;
            // 
            // button2
            // 
            button2.Location = new Point(149, 160);
            button2.Name = "button2";
            button2.Size = new Size(75, 23);
            button2.TabIndex = 1;
            button2.Text = "뒤로가기";
            button2.UseVisualStyleBackColor = true;
            button2.Click += Back_Click;
            // 
            // ID_Create
            // 
            ID_Create.Location = new Point(74, 37);
            ID_Create.Name = "ID_Create";
            ID_Create.Size = new Size(100, 23);
            ID_Create.TabIndex = 2;
            // 
            // PW_Create
            // 
            PW_Create.Location = new Point(74, 75);
            PW_Create.Name = "PW_Create";
            PW_Create.Size = new Size(100, 23);
            PW_Create.TabIndex = 3;
            // 
            // ID
            // 
            ID.AutoSize = true;
            ID.Location = new Point(29, 45);
            ID.Name = "ID";
            ID.Size = new Size(19, 15);
            ID.TabIndex = 4;
            ID.Text = "ID";
            ID.Click += ID_Click;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(12, 83);
            label2.Name = "label2";
            label2.Size = new Size(57, 15);
            label2.TabIndex = 5;
            label2.Text = "Password";
            // 
            // CreateUser
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(label2);
            Controls.Add(ID);
            Controls.Add(PW_Create);
            Controls.Add(ID_Create);
            Controls.Add(button2);
            Controls.Add(button1);
            Name = "CreateUser";
            Text = "CreateUser";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button button1;
        private Button button2;
        private TextBox ID_Create;
        private TextBox PW_Create;
        private Label ID;
        private Label label2;
    }
}