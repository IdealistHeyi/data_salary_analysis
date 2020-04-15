import tkinter as tk
import tkinter.messagebox
from salaryAnalysis.income_compare import IncomeCompare
from salaryAnalysis.post_express_distribution_structural import StructuralAnalysis
from salaryAnalysis.post_express_distribution_structural import PostalExpressCompare
from salaryAnalysis.post_express_distribution_structural import Distribution
from salaryAnalysis.allot_relation import AllotRelation
from salaryAnalysis.all_data_processing import AnnualSalary


class AppUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("数据可视化软件_百张图表瞬间完成_作者微信：heyipost")
        self.root.iconbitmap("i.ico")
        self.create_menu()
        self.create_content()
        self.root.geometry('450x558')
        self.root.mainloop()

    def create_menu(self):
        """该函数为设置菜单栏，变量名 menu_bar """
        """增加菜单栏"""
        menu_bar = tk.Menu(self.root)

        """增加文件菜单"""
        file_menu = tk.Menu(menu_bar, tearoff=0, font=("楷体", 10,))
        menu_bar.add_cascade(label="文件", menu=file_menu, font=("楷体", 10,))
        """增加文件菜单里的命令"""
        file_menu.add_command(label="命令选项", command=self.root.quit, font=("楷体", 10,))
        file_menu.add_separator()
        file_menu.add_command(label="退出程序", command=self.root.quit, font=("楷体", 10,))
        """-----------------------"""

        """增加运行菜单"""
        run_menu = tk.Menu(menu_bar, tearoff=0, font=("楷体", 10,))
        menu_bar.add_cascade(label="运行", menu=run_menu, font=("楷体", 10,))
        """增加文件菜单里的命令"""
        run_menu.add_command(label="数据预处理_全口径收入", command=AnnualSalary.main_all, font=("楷体", 10,))
        run_menu.add_command(label="数据预处理_工资总额", command=AnnualSalary.main_gz, font=("楷体", 10,))
        run_menu.add_separator()
        run_menu.add_command(label="薪酬结构分析", command=StructuralAnalysis.main, font=("楷体", 10,))
        run_menu.add_command(label="薪酬极值分布分析", command=Distribution, font=("楷体", 10,))
        run_menu.add_command(label="分配关系分析", command=AllotRelation, font=("楷体", 10,))
        run_menu.add_command(label="各岗位、专业薪酬分析", command=IncomeCompare.main, font=("楷体", 10,))
        run_menu.add_command(label="邮速对比分析", command=PostalExpressCompare.main, font=("楷体", 10,))
        """-----------------------"""

        """增加关于菜单"""
        about_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="关于", menu=about_menu)
        """增加关于菜单里的命令"""
        about_menu.add_command(label="version:1.0", font=("楷体", 10,))
        about_menu.add_separator()

        """-----------------------"""

        """增加退出菜单"""
        exit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="退出", menu=exit_menu)
        """增加关于退出里的命令"""
        exit_menu.add_command(label="exit", command=self.root.quit, font=("楷体", 12,))
        exit_menu.add_separator()
        """-----------------------"""

        """增加帮助菜单"""
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="帮助文档", menu=help_menu)
        """增加关于菜单里的命令"""
        help_menu.add_command(label="帮助文档", font=("楷体", 10,),command=AppUI.help)
        help_menu.add_separator()
        help_menu.add_command(label="免费使用，遇问题可咨询作者，QQ: 330603182 ", command=self.root.quit, font=("楷体", 10,))
        """-----------------------"""

        self.root.config(menu=menu_bar)

    def create_content(self):

        """-----------------数据预处理----------------"""
        tk.Label(self.root, text="    对于从系统查询节点\n导出的文件集，进行数据\n清洗处理，处理后每人每\n月一条记录，基础信息为"
                                 + "\n当月工资关系所属单位的\n基础信息，30万条运行时\n间10分钟，请耐心等待。", font=("楷体", 11,), foreground='green')\
            .place(x=25, y=13, width=190, height=103)
        tk.Button(self.root, text="数据处理_全部收入", font=("微软雅黑", 10,), command=AnnualSalary.main_all, foreground='green').place(x=288, y=22, width=127, height=37)
        tk.Button(self.root, text="数据处理_工资总额", font=("微软雅黑", 10,), command=AnnualSalary.main_gz, foreground='green').place(x=288, y=72, width=127, height=37)

        tk.Label(self.root, text="----->", font=("楷体", 11,), foreground='green').place(x=220, y=60, width=60, height=25)
        tk.Label(self.root, text="执行", font=("楷体", 11,), foreground='green').place(x=228, y=50, width=38, height=20)

        separator = tk.Frame(self.root, height=1, width=5, bd=1, bg="red", relief=tk.GROOVE)
        separator.place(x=25, y=127, width=400, height=2)  # pack(fill=X, padx=5, pady=5)
        """------------------------------------"""

        """-------------结构分析---------------"""
        down = 120
        tk.Label(self.root, text="    数据预处理运行一次\n后，即可进行下面数据的\n可视化呈现，点击此处可\n进行薪酬结构的分析。以\n下运行时间均小于20秒。", font=("楷体", 11,), foreground='blue').place(x=25, y=13+down, width=190, height=90)
        tk.Button(self.root, text="薪酬结构分析", font=("微软雅黑", 11,), command=StructuralAnalysis.main, foreground='blue').place(x=295, y=45+down, width=110, height=40)

        tk.Label(self.root, text="----->", font=("楷体", 11,), foreground='blue').place(x=220, y=60+down, width=60, height=25)
        tk.Label(self.root, text="执行", font=("楷体", 11,), foreground='blue').place(x=228, y=50+down, width=38, height=20)

        """------------------------------------"""
        down_y = 80
        """-------------薪酬分布分析---------------"""
        down = down+down_y
        tk.Label(self.root, text="    点击此处呈现薪酬分\n布情况，呈现范围可为全\n省（区）、各市分公司、\n各岗位序列等。        ",
                 font=("楷体", 11,), foreground='blue').place(x=25, y=13+down, width=190, height=90)
        tk.Button(self.root, text="极值分布分析", font=("微软雅黑", 11,), command=Distribution, foreground='blue')\
            .place(x=295, y=45+down, width=110, height=40)
        tk.Label(self.root, text="----->", font=("楷体", 11,), foreground='blue').place(x=220, y=60+down, width=60, height=25)
        tk.Label(self.root, text="执行", font=("楷体", 11,), foreground='blue').place(x=228, y=50+down, width=38, height=20)

        """------------------------------------"""

        """-------------分配关系分析---------------"""
        down = down+down_y
        tk.Label(self.root, text="    点击此处呈现各岗位\n各职级薪酬倍比情况，呈\n现范围为全省（区）、各\n市分公司等。",
                 font=("楷体", 11,), justify="left", foreground='blue').place(x=25, y=13+down, width=190, height=90)
        tk.Button(self.root, text="分配关系分析", font=("微软雅黑", 11,), command=AllotRelation, foreground='blue')\
            .place(x=295, y=45+down, width=110, height=40)
        tk.Label(self.root, text="----->", font=("楷体", 11,), foreground='blue').place(x=220, y=60+down, width=60, height=25)
        tk.Label(self.root, text="执行", font=("楷体", 11,), foreground='blue').place(x=228, y=50+down, width=38, height=20)

        """------------------------------------"""

        """-------------岗位薪酬分析---------------"""
        down = down+down_y
        tk.Label(self.root, text="    点击此处对各专业、\n各岗位的薪酬情况进行对\n比分析，呈现范围可为全\n省（区）、各市分公司。",
                 font=("楷体", 11,), foreground='blue', justify="left").place(x=25, y=13+down, width=190, height=90)
        tk.Button(self.root, text="岗位\专业分析", font=("微软雅黑", 11,), command=IncomeCompare.main, foreground='blue')\
            .place(x=295, y=45+down, width=110, height=40)
        tk.Label(self.root, text="----->", font=("楷体", 11,), foreground='blue').place(x=220, y=60+down, width=60, height=25)
        tk.Label(self.root, text="执行", font=("楷体", 11,), foreground='blue').place(x=228, y=50+down, width=38, height=20)

        """------------------------------------"""

        """-------------邮速对比分析---------------"""
        down = down+down_y
        tk.Label(self.root, text="    点击此处对邮、速双\n方薪酬进行对比分析，呈\n现范围全省（区）、各市\n分公司。",
                 font=("楷体", 11,), foreground='blue', justify="left").place(x=25, y=13+down, width=190, height=90)
        tk.Button(self.root, text="邮速对比分析", font=("微软雅黑", 11,), command=PostalExpressCompare.main, foreground='blue')\
            .place(x=295, y=45+down, width=110, height=40)
        tk.Label(self.root, text="----->", font=("楷体", 11,), foreground='blue').place(x=220, y=60+down, width=60, height=25)
        tk.Label(self.root, text="执行", font=("楷体", 11,), foreground='blue').place(x=228, y=50+down, width=38, height=20)

        """------------------------------------"""

    @staticmethod
    def help():
        tk.messagebox.showinfo(title="操作指南", message="第一步：按以下步骤 从HR系统 的人员薪酬明细查询节点的人员薪酬明细查询导出薪酬明细"
                                                     "数据，导出的文件可能达到1000多文件，但不妨事，一起放到程序包中的<系统导出的明细数据>这个文件夹中，"
                                                     "数据由程序清洗处理，处理后每人每月一条记录，人员的岗位、职务等基础信息为当月该人员在工资关系所属单位的基础信息，数据处理只需要运行"
                                                     "一次，以后自动生成出图表就不需要运行数据处理这一步了，数据处理生成的数据是计算机自动生成图表的数据依据。\n\n "
                                                     "第二步：如下图，配置程序包中的薪酬分析的设"
                                                     "置信息.xlsx文件，就是把其中的第一个工作表《机构信息设置》填一下，就是你从系统导出的大量数据"
                                                     "只有实帐单位名称，只有一一对应所属市公司名称，程序才能进行归类对比分析！其他2个工作表都配置"
                                                     "好了，不要填了。\n\n第三步：点击程序包中的main.exe 文件，启动程序，先选一种方式 点击 绿色文字的按钮 把数据处理"
                                                     "一下，然后点击蓝色文字的按钮就可以出分析图表了，50至100张薪酬分析图表瞬间完成，以后换了数据也可以"
                                                     "生成不同的分析图表了，解放劳动力！！\n\n         具体请看操作指南的 Word 文档 和 操作讲解视频！ ")


if __name__ == '__main__':
    AppUI()


