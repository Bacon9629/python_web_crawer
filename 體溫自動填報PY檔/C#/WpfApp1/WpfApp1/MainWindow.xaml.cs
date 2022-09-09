using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WpfApp1
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            StreamReader reader = new StreamReader("accountInformation.inf");
            String[] r = reader.ReadLine().Split(",");
            id_edit.Text = r[0];
            pass_edit.Text = r[1];
            reader.Close();
        }

        private void oneDay_bt_Click(object sender, RoutedEventArgs e)
        {
            runEXE("oneDay.exe");
        }

        private void runEXE(String fileName)
        {
            StreamWriter writer = new StreamWriter("accountInformation.inf");
            writer.WriteLine(id_edit.Text+","+ pass_edit.Text);
            writer.Close();

            Process p = new Process();
            String str = null;

            p.StartInfo.FileName = fileName;

            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = true; //不跳出cmd視窗

            p.Start();
            //p.StandardInput.WriteLine("oneDay.exe");
            p.StandardInput.WriteLine(id_edit.Text);
            p.StandardInput.WriteLine(pass_edit.Text);
            //p.StandardInput.WriteLine("exit");
            //p.StandardInput.WriteLine("exit");

            str = p.StandardOutput.ReadToEnd();
            p.WaitForExit();
            p.Close();

            detail_tb.Text = str;
        }

        private void allDay_bt_Click(object sender, RoutedEventArgs e)
        {
            runEXE("allDay.exe");
        }
    }
}
