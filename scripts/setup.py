"""
Article Gen - 安装配置脚本
运行此脚本完成环境配置
"""
import os
import sys
import subprocess
import shutil

def main():
    print("=" * 50)
    print("  Article Gen - 公众号文章生成器 安装")
    print("=" * 50)
    print()

    # 检查 Python 版本
    if sys.version_info < (3, 10):
        print("❌ 需要 Python 3.10+，当前版本:", sys.version)
        sys.exit(1)
    print(f"✅ Python 版本: {sys.version.split()[0]}")

    # 检查 git
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        print("✅ Git 已安装")
    except FileNotFoundError:
        print("❌ 未找到 Git，请先安装 Git")
        sys.exit(1)

    # 克隆 ForgeRSS
    forge_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "forge-rss")
    if not os.path.exists(forge_dir):
        print("\n📦 正在克隆 ForgeRSS...")
        subprocess.run([
            "git", "clone", "--depth", "1",
            "https://github.com/tmwgsicp/ForgeRSS.git",
            forge_dir
        ], check=True)
        print("✅ ForgeRSS 克隆完成")
    else:
        print("✅ ForgeRSS 已存在")

    # 创建虚拟环境
    venv_dir = os.path.join(forge_dir, "venv")
    if not os.path.exists(venv_dir):
        print("\n📦 正在创建虚拟环境...")
        subprocess.run([sys.executable, "-m", "venv", venv_dir], check=True)
        print("✅ 虚拟环境创建完成")
    else:
        print("✅ 虚拟环境已存在")

    # 安装依赖
    print("\n📦 正在安装依赖...")
    pip_cmd = os.path.join(venv_dir, "Scripts" if os.name == "nt" else "bin", "pip")
    subprocess.run([pip_cmd, "install", "-r", os.path.join(forge_dir, "requirements.txt")], check=True)
    print("✅ 依赖安装完成")

    # 复制技能文件
    skills_src = os.path.join(os.path.dirname(os.path.dirname(__file__)), "skills", "gen-article.md")
    skills_dst_dir = os.path.join(os.path.expanduser("~"), ".claude", "skills")
    skills_dst = os.path.join(skills_dst_dir, "gen-article.md")

    os.makedirs(skills_dst_dir, exist_ok=True)
    shutil.copy2(skills_src, skills_dst)
    print(f"\n✅ 技能文件已复制到: {skills_dst}")

    print()
    print("=" * 50)
    print("  安装完成！")
    print("=" * 50)
    print()
    print("下一步：")
    print("  1. 登录小红书（首次需要扫码）：")
    if os.name == "nt":
        print(f"     cd forge-rss && venv\\Scripts\\python.exe -m generators.social.xiaohongshu.scraper --login")
    else:
        print(f"     cd forge-rss && venv/bin/python -m generators.social.xiaohongshu.scraper --login")
    print()
    print("  2. 登录知乎（首次需要扫码）：")
    if os.name == "nt":
        print(f"     venv\\Scripts\\python.exe -m generators.social.zhihu.scraper --login")
    else:
        print(f"     venv/bin/python -m generators.social.zhihu.scraper --login")
    print()
    print("  3. 使用技能：")
    print("     在 Claude Code 中输入: /gen-article 情感 300字 倾诉型")
    print()

if __name__ == "__main__":
    main()
