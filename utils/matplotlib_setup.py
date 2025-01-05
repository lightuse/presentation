import matplotlib.pyplot as plt

def setup_matplotlib_for_environment():
    """
    環境に応じて適切な matplotlib の設定を行う
    """
    try:
        get_ipython()
        # Jupyter環境の場合
        get_ipython().run_line_magic('matplotlib', 'inline')
        plt.style.use('default')  # デフォルトスタイルを使用
    except:
        # スクリプト実行の場合
        import matplotlib
        matplotlib.use('Agg')
        plt.style.use('default')  # デフォルトスタイルを使用

def save_or_show_plot(fig, filename=None):
    """
    環境に応じて適切な方法でプロットを表示または保存
    
    Args:
        fig: matplotlib の Figure オブジェクト
        filename: 保存する場合のファイル名（オプション）
    """
    try:
        get_ipython()
        # Jupyter環境の場合は表示
        plt.show()
    except:
        # スクリプト実行の場合は保存
        if filename:
            fig.savefig(filename, bbox_inches='tight', dpi=300)
        else:
            fig.savefig('plot.png', bbox_inches='tight', dpi=300)