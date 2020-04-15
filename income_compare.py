# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as m_ticker
from .public_data_processing import InitData
import time
import sys

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['STKait', 'SimHei', 'Microsoft YaHei', 'KaiTi',  'STXihei']


"""岗位序列及专业薪酬分析"""
# --------公共类部分------------


class IncomeCompare:

    @staticmethod
    def paint(month, year, company, company_directly_under, df_AB_L):

        month = ""

        for i in range(2):
            if i == 0:
                category = "市分公司"
                try:
                    df_AB = df_AB_L.loc[df_AB_L['所属市公司名称'] == company[0], :]
                except IndexError:
                    InitData.message_direct()
                for ii in range(1, len(company), 1):
                    df_AB = df_AB.append(df_AB_L.loc[df_AB_L['所属市公司名称'] == company[ii], :])
            else:
                category = "直属单位"
                try:
                    df_AB = df_AB_L.loc[df_AB_L['所属市公司名称'] == company_directly_under[0], :]
                except IndexError:
                    InitData.message_direct()
                for ii in range(1, len(company_directly_under), 1):
                    df_AB = df_AB.append(df_AB_L.loc[df_AB_L['所属市公司名称'] == company_directly_under[ii], :])

            """生成数据透视表"""
            groups_ps = df_AB.groupby(['所属市公司名称', '主序列'])
            应发合计平均值 = groups_ps['应发合计'].mean().round(2)
            实发合计平均值 = groups_ps['实发合计'].mean().round(2)
            业务发展奖平均值 = groups_ps['业务发展和营销积分奖'].mean().round(2)

            df_AB_DWXL = pd.DataFrame({'应发合计平均值': 应发合计平均值, '实发合计平均值': 实发合计平均值,
                                       '业务发展奖平均值': 业务发展奖平均值})

            df_AB_DWXL['dwxl'] = df_AB_DWXL.index
            yf_list = df_AB_DWXL['应发合计平均值'].values.tolist()
            list_max = max(yf_list)



            def dw(x):
                x1, x2 = x
                return x1

            def xl(x):
                x1, x2 = x
                return x2

            def px(x, x_index_ls):
                for i in range(len(x_index_ls)):
                    if x == x_index_ls[i]:
                        return i

            df_AB_DWXL['dw'] = df_AB_DWXL['dwxl'].apply(dw)  # .str.split('',expand=True)[0]
            df_AB_DWXL['xl'] = df_AB_DWXL['dwxl'].apply(xl)

            """排序"""
            df_ls = df_AB_DWXL.loc[df_AB_DWXL['xl'] == '管理序列', :]
            df_ls = df_ls.sort_values(by=['应发合计平均值'], ascending=[True])
            x_index_ls = df_ls['dw'].drop_duplicates().values.tolist()
            df_AB_DWXL['xh'] = df_AB_DWXL['dw'].apply(px, args=(x_index_ls,))
            df_AB_DWXL = df_AB_DWXL.sort_values(by=['xh'], ascending=[False])
            print(df_AB_DWXL)

            #     df_AB_DWXL=df_AB_DWXL.reset_index(drop=True) #  重新索引

            x_index_label = df_AB_DWXL['dw'].drop_duplicates().values.tolist()
            x_index = np.arange(len(x_index_label))  # x轴序列长度
            print(x_index, "$$$$$$$$$$$$", x_index_label)

            """生成图表用数据"""
            x_yf_manage = df_AB_DWXL.loc[df_AB_DWXL['xl'] == "管理序列", :]['应发合计平均值']  # &| 的使用
            x_yw_manage = df_AB_DWXL.loc[df_AB_DWXL['xl'] == "管理序列", :]['业务发展奖平均值']  # &| 的使用

            df_AB_DWXL_index = df_AB_DWXL.loc[df_AB_DWXL['xl'] == "管理序列", :]['dw'].drop_duplicates().values.tolist()
            # df_AB_DWXL_index = [x1 for x1,x2 in df_AB_DWXL_index ]
            if len(x_index_label) != len(df_AB_DWXL_index):
                x_yf_manage = np.array(x_yf_manage)
                x_yw_manage = np.array(x_yw_manage)
                for j in range(len(x_index_label)):
                    if x_index_label[j] not in df_AB_DWXL_index:
                        x_yf_manage = np.insert(x_yf_manage, j, 0)  # 表示在ndarray x的第j个位置插入0
                        x_yw_manage = np.insert(x_yw_manage, j, 0)  # 表示在ndarray x的第j个位置插入0

            x_yf_profession = df_AB_DWXL.loc[df_AB_DWXL['xl'] == "专业序列", :]['应发合计平均值']  # &| 的使用
            x_yw_profession = df_AB_DWXL.loc[df_AB_DWXL['xl'] == "专业序列", :]['业务发展奖平均值']  # &| 的使用
            df_AB_DWXL_index = df_AB_DWXL.loc[df_AB_DWXL['xl'] == "专业序列", :]['dw'].drop_duplicates().values.tolist()
            if len(x_index_label) != len(df_AB_DWXL_index):
                x_yf_profession = np.array(x_yf_profession)
                x_yw_profession = np.array(x_yw_profession)
                for j in range(len(x_index_label)):
                    if x_index_label[j] not in df_AB_DWXL_index:
                        x_yf_profession = np.insert(x_yf_profession, j, 0)  # 表示在ndarray x的第j个位置插入0
                        x_yw_profession = np.insert(x_yw_profession, j, 0)  # 表示在ndarray x的第j个位置插入0

            x_yf_operate = df_AB_DWXL.loc[df_AB_DWXL['xl'] == "操作序列", :]['应发合计平均值']  # &| 的使用
            x_yw_operate = df_AB_DWXL.loc[df_AB_DWXL['xl'] == "操作序列", :]['业务发展奖平均值']  # &| 的使用
            df_AB_DWXL_index = df_AB_DWXL.loc[df_AB_DWXL['xl'] == "操作序列", :]['dw'].drop_duplicates().values.tolist()
            if len(x_index_label) != len(df_AB_DWXL_index):
                x_yf_operate = np.array(x_yf_operate)
                x_yw_operate = np.array(x_yw_operate)
                for j in range(len(x_index_label)):
                    if x_index_label[j] not in df_AB_DWXL_index:
                        x_yf_operate = np.insert(x_yf_operate, j, 0)  # 表示在ndarray x的第j个位置插入0
                        x_yw_operate = np.insert(x_yw_operate, j, 0)  # 表示在ndarray x的第j个位置插入0

            figure_size = 24, 15  # 设置输出的图片大小
            # fig, ax = plt.subplots(figsize=figure_size)

            plt.figure(figsize=figure_size)
            ax = plt.gca()
            fig = plt.gcf()

            bar_width = 0.25  # 柱状宽度
            bar_width_yw = 0.15

            """生成柱状图序列"""
            yf_manage = plt.bar(x_index, x_yf_manage, width=bar_width, alpha=0.9, label='应发合计平均值',
                                color='#000093')  ##613030 color='r'cadetblue,
            yw_manage = plt.bar(x_index, x_yw_manage, width=bar_width_yw, alpha=1, label='业务发展奖平均值',
                                color='r')  # color='r',

            yf_profession = plt.bar(x_index + bar_width, x_yf_profession, width=bar_width, alpha=0.8, label='应发合计平均值',
                                    color='#0000E3')  # #484891color='r',steelblue
            yw_profession = plt.bar(x_index + bar_width_yw + (bar_width - bar_width_yw), x_yw_profession,
                                    width=bar_width_yw, alpha=1, label='业务发展奖平均值', color='r')  # color='r',

            yf_operate = plt.bar(x_index + bar_width * 2, x_yf_operate, width=bar_width, alpha=1, label='应发合计平均值',
                                 color='#6A6AFF')  # color='r',
            yw_operate = plt.bar(x_index + (bar_width_yw + (bar_width - bar_width_yw)) * 2, x_yw_operate,
                                 width=bar_width_yw, alpha=1, label='业务发展奖平均值', color='r')  # color='r',

            """X坐标轴设置"""
            fs = 12 if i == 0 else 12
            plt.xticks(x_index + bar_width, x_index_label, rotation=15, fontsize=fs, ha="right")  # 用处理好的数据来设置X轴的刻度

            """Y坐标轴设置"""
            # ax.locator_params('y', nbins=6)  # 设置Y轴的范围为6个区间
            # plt.axis([-1, 75, 0, list_max+5000])  # 设置坐标轴范围
            plt.yticks(fontsize=12)
            ax.yaxis.set_major_formatter(m_ticker.FormatStrFormatter('%.f 元'))  # 将Y轴的刻度加单位元
            ax.yaxis.grid(True, which='major', color='silver', linestyle='--', linewidth=1, alpha=0.3)  # 加Y轴的网格线

            """图例及标签设置"""
            plt.legend(handles=[yf_manage, yf_profession, yf_operate, yw_manage],
                       labels=['管理序列员工应发合计平均值', '专业序列员工应发合计平均值', '操作序列员工应发合计平均值', '各序列员工业务发展奖平均值'], loc='best',
                       # bbox_to_anchor=(0,0),
                       prop={'size': 11}, frameon=True)  # 图例设置 fontsize=15,'family': regular,
            # ax.set_xlabel("全省" + category + "及其岗位序列（含寄递事业部）", fontsize=12)  # 可以用plt.xlabel(), fontproperties=circle
            plt.text(len(x_index_label)/2, list_max*1.09, "(含寄递事业部)", size=16, ha='center')
            print("___------_____", list_max-10000, len(x_index_label)/2)
            ax.set_ylabel("员工收入", fontsize=12)  # 可以用plt.ylabel(), fontproperties=regular,
            table_name = "全省" + category + "合同用工" + year + month + "管理、专业、操作序列人均薪酬分析对比柱状图"

            """布局设置"""
            # ax.set_xlim(-1,len(x_index))
            ax.set_ylim(0, list_max*1.2)
            # plt.tight_layout()  # 紧凑型布局
            if i == 0:  # 市公司
                top = 0.993
                bottom = 0.133
                left = 0.075
                right = 0.977
                hspace = 0.2
                wspace = 0.2
            else:  # 直属单位
                top = 0.993
                bottom = 0.153
                left = 0.075
                right = 0.975
                hspace = 0.2
                wspace = 0.2
            fig.subplots_adjust(left=left, bottom=bottom, top=top, right=right, wspace=wspace, hspace=hspace)  # 布局设置
            fig.suptitle(table_name, fontsize=16)  # , x=2, y=1.03 fontproperties=yahei,
            # ax.set_title(table_name, fontsize=10)  # 用plt.title()总标题不显示  ax.set_title(table_name)
            plt.show()
            InitData.save(fig, table_name)

    @staticmethod
    def extract_data(df):
        """提取年度和月份--"""
        col = df.columns
        if '年' in col:
            year = str(int(df.loc[1, '年'])) + "年度"
        else:
            year = ""

        if '月' in col:
            month = str(int(df.loc[1, '月'])) + "月份"
        else:
            month = ""

        """提取AB类员工数据--"""
        #     df[df.E.isin(['aa'])|df.E.isin(['cc'])] # isnotin   df[df.isin({'D':[0,3],'E':['aa','cc']})]

        df_yes = df[df['人员类别'].isin(['合同用工A类', '合同用工B类'])]

        #  df_yes = df.loc[(df['人员类别'] == '合同用工A类')|(df['人员类别'] == '合同用工B类'),:]
        #  ----------------------------------

        # 不去改非的三级人员
        #  df_yes = df_yes.loc[~((df_yes['过渡岗位序列'] == '管理')&((df_yes['职务级别'] == '三级正')|(df_yes['职务级别'] == '三级副')
        #                                                      |(df_yes['职务级别'] == '二级副')|(df_yes['职务级别'] == '二级正'))),:]

        # 去改非的三级人员
        # df_yes = df_yes.loc[~((df_yes['职务级别'] == '三级正')|(df_yes['职务级别'] == '三级副')|
        #                                    (df_yes['职务级别'] == '二级副')|(df_yes['职务级别'] == '二级正')),:]
        del df

        """提取AB类员工的相应单位类别数据--"""
        company_total = df_yes['所属市公司名称'].drop_duplicates().values.tolist()
        company = [x for x in company_total if "市分公司" in x or "州分公司" in x or "地区分公司" in x]  # 市公司
        company_directly_under = [x for x in company_total if x not in company]  # 省直属单位

        print(company, company_directly_under)
        return month, year, company, company_directly_under, df_yes

    @staticmethod
    def paint_post(year, scope, df):

        """生成数据透视表"""

        groups_ps = df.groupby(['过渡岗位序列'])
        应发合计平均值 = groups_ps['应发合计'].mean().round(2)
        业务发展奖平均值 = groups_ps['业务发展和营销积分奖'].mean().round(2)

        df_AB_DWXL = pd.DataFrame({'应发合计平均值': 应发合计平均值,
                                   '业务发展奖平均值': 业务发展奖平均值})

        df_AB_DWXL['应发合计平均值'] = df_AB_DWXL['应发合计平均值']*12
        df_AB_DWXL['业务发展奖平均值'] = df_AB_DWXL['业务发展奖平均值']*12

        df_AB_DWXL['dwxl'] = df_AB_DWXL.index
        df_AB_DWXL.sort_values(by='应发合计平均值', ascending=True, inplace=True)

        x_index_label = df_AB_DWXL['dwxl'].drop_duplicates().values.tolist()
        x_index = np.arange(len(x_index_label))  # x轴序列长度
        print(x_index, "$$$$$$$$$$$$", x_index_label)

        """生成图表用数据"""
        x_yf_manage = df_AB_DWXL['应发合计平均值']  # &| 的使用
        x_yw_manage = df_AB_DWXL['业务发展奖平均值']  # &| 的使用

        figure_size = 24, 18  # 设置输出的图片大小
        plt.figure(figsize=figure_size)
        ax = plt.gca()
        fig = plt.gcf()

        bar_width = 0.618  # 柱状宽度width
        bar_width_yw = 0.35

        """生成柱状图序列"""
        yf_manage = plt.barh(x_index, x_yf_manage, height=bar_width, alpha=0.6, label='应发合计平均值',
                             color='#000093')  ##613030 color='r'cadetblue,
        yw_manage = plt.barh(x_index, x_yw_manage, height=bar_width_yw, alpha=0.9, label='业务发展奖平均值',
                             color='r')  # color='r',

        """X坐标轴设置"""
        plt.yticks(x_index, x_index_label, rotation=0, fontsize=12, ha="right")  # 用处理好的数据来设置X轴的刻度

        """Y坐标轴设置"""
        # ax.locator_params('y', nbins=6)  # 设置Y轴的范围为6个区间
        # plt.axis([-1, 75, 0, list_max+5000])  # 设置坐标轴范围
        plt.xticks(fontsize=12)
        ax.xaxis.set_major_formatter(m_ticker.FormatStrFormatter('%.f 元'))  # 将Y轴的刻度加单位元
        ax.xaxis.grid(True, which='major', color='silver', linestyle='--', linewidth=1, alpha=0.3)  # 加Y轴的网格线

        """图例及标签设置"""
        plt.legend(handles=[yf_manage, yw_manage], labels=['各岗位序列员工年均薪酬', '各岗位序列员工年均业务发展奖'], loc='right',
                   # bbox_to_anchor=(0,0),
                   prop={'size': 12}, frameon=True)  # 图例设置 fontsize=15,'family': regular,
        #plt.ylabel("全省" + "各岗位序列（含寄递事业部）", fontsize=12)  # 可以用plt.xlabel(), fontproperties=circle
        plt.xlabel("员工收入", fontsize=12)  # 可以用plt.ylabel(), fontproperties=regular,

        # table_name = "全省合同用工"+" 20" + str(datetime.datetime.now().strftime('%y'))+"年"+str(datetime.datetime.now().strftime('%m')) + \
        #              "月份 "+"操作序列、专业序列、管理序列员工平均应发、实发和业务发展奖分析对比柱状图"
        table_name = year + scope + "各岗位序列员工年均薪酬及业务发展奖分析对比柱状图"

        """布局设置"""
        # ax.set_xlim(-1,list_max*1.2)
        ax.set_ylim(0 - 1, len(x_index) + 1.3)
        top = 0.991
        bottom = 0.116
        left = 0.146
        right = 0.947
        hspace = 0.2
        wspace = 0.2
        #plt.tight_layout()  # 紧凑型布局
        fig.subplots_adjust(left=left, bottom=bottom, top=top, right=right, wspace=wspace, hspace=hspace)  # 布局设置
        fig.suptitle(table_name, fontsize=16)  # , x=2, y=1.03 fontproperties=yahei,
        #  ax.set_title(table_name, fontsize=15)  # 用plt.title()总标题不显示  ax.set_title(table_name)
        plt.show()
        InitData.save(fig,table_name)
        # fig.savefig('D:\\img\\' + table_name + 'h.pdf', dpi=600)

    @staticmethod
    def paint_profession(year, scope, df):

        """生成数据透视表"""
        groups_ps = df.groupby(['专业类别'])
        应发合计平均值 = groups_ps['应发合计'].mean().round(2)
        业务发展奖平均值 = groups_ps['业务发展和营销积分奖'].mean().round(2)

        df_AB_DWXL = pd.DataFrame({'应发合计平均值': 应发合计平均值,
                                   '业务发展奖平均值': 业务发展奖平均值})

        df_AB_DWXL['应发合计平均值'] = df_AB_DWXL['应发合计平均值']*12
        df_AB_DWXL['业务发展奖平均值'] = df_AB_DWXL['业务发展奖平均值']*12

        df_AB_DWXL['dwxl'] = df_AB_DWXL.index
        df_AB_DWXL.sort_values(by='应发合计平均值', ascending=True, inplace=True)

        x_index_label = df_AB_DWXL['dwxl'].drop_duplicates().values.tolist()
        x_index = np.arange(len(x_index_label))  # x轴序列长度
        print(x_index, "$$$$$$$$$$$$", x_index_label)

        """生成图表用数据"""
        x_yf_manage = df_AB_DWXL['应发合计平均值']  # &| 的使用
        x_yw_manage = df_AB_DWXL['业务发展奖平均值']  # &| 的使用

        figure_size = 24, 18  # 设置输出的图片大小
        plt.figure(figsize=figure_size)
        ax = plt.gca()
        fig = plt.gcf()

        bar_width = 0.618  # 柱状宽度width
        bar_width_yw = 0.35

        """生成柱状图序列"""
        yf_manage = plt.barh(x_index, x_yf_manage, height=bar_width, alpha=0.6, label='应发合计平均值',
                             color='#000093')  ##613030 color='r'cadetblue,
        yw_manage = plt.barh(x_index, x_yw_manage, height=bar_width_yw, alpha=0.9, label='业务发展奖平均值',
                             color='r')  # color='r',

        """X坐标轴设置"""
        plt.yticks(x_index, x_index_label, rotation=0, fontsize=12, ha="right")  # 用处理好的数据来设置X轴的刻度

        """Y坐标轴设置"""
        # ax.locator_params('y', nbins=6)  # 设置Y轴的范围为6个区间
        # plt.axis([-1, 75, 0, list_max+5000])  # 设置坐标轴范围
        plt.xticks(fontsize=12)
        ax.xaxis.set_major_formatter(m_ticker.FormatStrFormatter('%.f 元'))  # 将Y轴的刻度加单位元
        ax.xaxis.grid(True, which='major', color='silver', linestyle='--', linewidth=1, alpha=0.3)  # 加Y轴的网格线

        """图例及标签设置"""
        plt.legend(handles=[yf_manage, yw_manage], labels=['各专业类别员工年均薪酬', '各专业类别员工年均业务发展奖'], loc='right',
                   # bbox_to_anchor=(0,0),
                   prop={'size': 12}, frameon=True)  # 图例设置 fontsize=15,'family': regular,
        #plt.ylabel("全省" + "各专业类别（含寄递事业部）", fontsize=12)  # 可以用plt.xlabel(), fontproperties=circle
        plt.xlabel("员工收入", fontsize=12)  # 可以用plt.ylabel(), fontproperties=regular,

        # table_name = "全省合同用工"+" 20" + str(datetime.datetime.now().strftime('%y'))+"年"+str(datetime.datetime.now().strftime('%m')) + \
        #              "月份 "+"操作序列、专业序列、管理序列员工平均应发、实发和业务发展奖分析对比柱状图"
        table_name = year + scope + "各专业类别员工年均薪酬及业务发展奖分析对比柱状图"

        """布局设置"""
        ax.set_ylim(0 - 1, len(x_index) + 1)
        #  ax.set_xlim(-1,len(x_index))
        #  ax.set_ylim(0, list_max*1.2)

        top = 0.995
        bottom = 0.116
        left = 0.106
        right = 0.947
        hspace = 0.2
        wspace = 0.2
        # plt.tight_layout()  # 紧凑型布局
        fig.subplots_adjust(left=left, bottom=bottom, top=top, right=right, wspace=wspace, hspace=hspace)  # 布局设置
        fig.suptitle(table_name, fontsize=15)  # , x=2, y=1.03 fontproperties=yahei,
        #  ax.set_title(table_name, fontsize=10)  # 用plt.title()总标题不显示  ax.set_title(table_name)
        plt.show()
        InitData.save(fig,table_name)

        # fig.savefig('D:\\img\\' + table_name + 'h.pdf', dpi=600)

    @staticmethod
    def extract_data_post(categroy, df):

        """提取年度和月份--"""
        col = df.columns
        if '年' in col:
            year = str(int(df.loc[1, '年'])) + "年度"
        else:
            year = ""

        """提取AB类员工数据--"""
        #     df[df.E.isin(['aa'])|df.E.isin(['cc'])] # isnotin   df[df.isin({'D':[0,3],'E':['aa','cc']})]

        df_yes = df[df['人员类别'].isin(['合同用工A类', '合同用工B类'])]
        del df

        #     df_yes = df.loc[(df['人员类别'] == '合同用工A类')|(df['人员类别'] == '合同用工B类'),:]
        #  ----------------------------------
        # 去二级人员，不去改非的二级人员
        if categroy == "全省合同用工(不含二级领导)":
            df_yes = df_yes.loc[~((df_yes['过渡岗位序列'] == '管理') & ((df_yes['职务级别'] == '二级副') | (df_yes['职务级别'] == '二级正'))),
                     :]
            df_yes = df_yes.loc[
                     ~((df_yes['过渡岗位序列'] == '综合职能') & ((df_yes['职务级别'] == '三级副') | (df_yes['职务级别'] == '三级正'))), :]
            df_yes = df_yes.loc[~((df_yes['过渡岗位序列'] == '综合职能') & (
                        (df_yes['职务级别'] == '副科级') | (df_yes['职务级别'] == '正科级') | (df_yes['职务级别'] == '三级1') | (
                            df_yes['职务级别'] == '三级2'))), :]
        #     elif categroy == "全省支局、所负责人":
        #         df_yes = df_yes.loc[df_yes['过渡岗位序列']=="生产主管",:]
        #     elif categroy == "全省三级领导人员":
        #         df_yes = df_yes.loc[((df_yes['过渡岗位序列'] == '管理')&((df_yes['职务级别'] == '三级副')|(df_yes['职务级别'] == '三级正'))),:]
        #     elif categroy == "全省四级领导人员":
        #         df_yes = df_yes.loc[((df_yes['过渡岗位序列'] == '管理')&(df_yes['职务级别'].isin(['正科级','副科级','三级1','三级2']))),:]
        else:
            sys.exit()

        # df_yes.to_excel('D:\\img\\xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.xlsx')

        # 去改非的三级人员
        # df_yes = df_yes.loc[~((df_yes['职务级别'] == '三级正')|(df_yes['职务级别'] == '三级副')|
        # (df_yes['职务级别'] == '二级副')|(df_yes['职务级别'] == '二级正')),:]
        return year, df_yes

    @staticmethod
    def extract_data_profession(categroy, df):

        """提取年度和月份--"""
        col = df.columns
        if '年' in col:
            year = str(int(df.loc[1, '年'])) + "年度"
        else:
            year = ""

        """提取AB类员工数据--"""
        #     df[df.E.isin(['aa'])|df.E.isin(['cc'])] # isnotin   df[df.isin({'D':[0,3],'E':['aa','cc']})]

        df_yes = df[df['人员类别'].isin(['合同用工A类', '合同用工B类'])]
        del df
        #  df_yes = df.loc[(df['人员类别'] == '合同用工A类')|(df['人员类别'] == '合同用工B类'),:]
        #  ----------------------------------
        # 去二级人员，不去改非的二级人员
        if categroy == "全省合同用工(不含二级领导)":
            df_yes = df_yes.loc[~((df_yes['过渡岗位序列'] == '管理') & ((df_yes['职务级别'] == '二级副') | (df_yes['职务级别'] == '二级正'))),
                     :]
            df_yes = df_yes.loc[
                     ~((df_yes['过渡岗位序列'] == '综合职能') & ((df_yes['职务级别'] == '三级副') | (df_yes['职务级别'] == '三级正'))), :]
            df_yes = df_yes.loc[~((df_yes['过渡岗位序列'] == '综合职能') & (
                        (df_yes['职务级别'] == '副科级') | (df_yes['职务级别'] == '正科级') | (df_yes['职务级别'] == '三级1') | (
                            df_yes['职务级别'] == '三级2'))), :]
        #     elif categroy == "全省支局、所负责人":
        #         df_yes = df_yes.loc[df_yes['过渡岗位序列']=="生产主管",:]
        #     elif categroy == "全省三级领导人员":
        #         df_yes = df_yes.loc[((df_yes['过渡岗位序列'] == '管理')&((df_yes['职务级别'] == '三级副')|(df_yes['职务级别'] == '三级正'))),:]
        #     elif categroy == "全省四级领导人员":
        #         df_yes = df_yes.loc[((df_yes['过渡岗位序列'] == '管理')&(df_yes['职务级别'].isin(['正科级','副科级','三级1','三级2']))),:]
        else:
            sys.exit()
        return year, df_yes

    @staticmethod
    def main():
        start = time.process_time()

        file_path = '.\\Detailed_annual_report_df.csv'
        read_List=['所属市公司名称','人员类别','应发合计','年','月','岗位','人员编码','职务级别','过渡岗位序列','业务发展和营销积分奖','专业类别', '划入来源']
        df = InitData.get_csv_df(file_path,read_List)

        #list_title = ['所属市公司名称','人员类别','年','月','岗位','人员编码','职务级别','专业类别','过渡岗位序列', '划入来源']
        #list_numeral = ['人员编码','应发合计','业务发展和营销积分奖']
        #data = InitData.merge_deduplicate_separately(df, list_title, list_numeral)

        scope = "全省合同用工(不含二级领导)"
        year, df = IncomeCompare.extract_data_profession(scope, df)
        IncomeCompare.paint_profession(year, scope, df)

        scope = "全省合同用工(不含二级领导)"
        year, df = IncomeCompare.extract_data_post(scope, df)
        IncomeCompare.paint_post(year, scope, df)

        """-----------%%%%%%%%%%%%%%-----------"""
        file_path = '.\\Detailed_annual_report_df.csv'
        option = ['所属市公司名称', '应发合计', '实发合计', '业务发展和营销积分奖', '主序列', '年', '月', '人员类别', '划入来源']
        data = InitData.get_csv_all_df(file_path, option)
        print("数据读取耗时% f" % (time.process_time() - start))

        extra_time = time.process_time()
        month, year, company, company_directly_under, df_yes = IncomeCompare.extract_data(data)
        print("提取数据耗时%f" % (time.process_time() - extra_time))
        print("总耗时%s" % (time.process_time() - start))

        char_time = time.process_time()
        IncomeCompare.paint(month, year, company, company_directly_under, df_yes)

        print("生成图标耗时%f" % (time.process_time() - char_time))
        print("总耗时%s" % (time.process_time() - start))


if __name__ == '__main__':
    IncomeCompare.main()

