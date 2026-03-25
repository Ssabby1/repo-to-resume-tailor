# Cursor 安装说明

## 推荐方式

Cursor 的规则是项目级的，所以需要指定目标项目：

```bash
pip install .
repo-to-resume-tailor init --ai cursor --project /path/to/your/project
```

备用方式：

```bash
python install.py --ai cursor --project /path/to/your/project
```

这会生成：

```text
/path/to/your/project/.cursor/rules/repo-to-resume-tailor.mdc
```

## 使用方式

安装完成后，在对应项目里调用 Cursor Agent，并使用类似下面的提示：

```text
Analyze this repository and write one resume-ready project description based only on repository evidence, tailored to the following role or JD, with a dedicated tech stack line.
```

生成的规则会保持与主 skill 一致的仓库分析和防夸大约束。
