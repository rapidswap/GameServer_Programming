using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace DummyClient
{
    internal static class Program
    {
        public static DummyClient mainForm_ = null;
        public static ProgramState programState_= null;
        /// <summary>
        ///  The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);

            mainForm_ = new DummyClient();
            programState_=new ProgramState();
            Application.Run(mainForm_);
            Application.Exit();
        }
    }
}