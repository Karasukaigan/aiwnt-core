# AIWNT Core

[English](./README.md)

![logo](./img/logo.webp)  

AIWNT（AI Web Novel Translator）是专为处理千万字级别超长网络小说的翻译而设计的工具。利用最新的大语言模型技术，消除网络小说跨语言传播的障碍，使全球读者无界限享受自己喜爱的作品。  

本项目是基于简单AI智能体构建的本地开源版本，它是对我们的[在线工作流（aiwnt.com）](https://www.aiwnt.com/)的一个简化版实现，但仍然保留了核心功能。您可以在自己的环境中部署和使用AIWNT，以实现高效、灵活的翻译操作。  

## 功能特性

- **高质量翻译结果**：基于大语言模型，其翻译质量大幅度优于传统机器翻译。
- **高效率处理能力**：针对超长文本优化，能够快速翻译千万字级别的内容。
- **简单易用**：没有复杂的部署流程，一行代码即可开始翻译。
- **本地化部署**：允许用户根据需要进行个性化定制，满足特定需求。

## 如何开始使用

如果您不希望自己部署，也可以试试我们功能更强大的[在线工作流](https://www.aiwnt.com/)。

按照以下步骤快速开启您的AIWNT之旅：

### 前提条件

- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [DeepSeek API Key](https://www.deepseek.com/)

### 步骤指南

1. **克隆到本地**
    ```
    git clone https://github.com/Karasukaigan/aiwnt-core.git
    ```
2. **安装OpenAI库**
    ```
    pip install openai
    ```
3. **配置global_config.json**  
    去掉`global_config.json.example`的`.example`后缀，然后编辑`global_config.json`，在`api_key`里填写您真实的API Key：  

    ```
    {
        "file_paths": {
            "output_directory": "output"
        },
        "api_config": {
            "base_url": "https://api.deepseek.com/v1",
            "api_key": "your_api_key_here",
            "model": "deepseek-chat"
        }
    }
    ```
4. **准备一个像这样的TXT文件**
    ```
    《代码修仙》
    简介：外卖骑手李凡意外穿越修真界，成为青云宗最底层的杂役弟子。在藏书阁打扫时，他发现修真界的阵法竟与计算机编程惊人相似。凭借编程功底，他参透阵法玄机，将代码思维与修真体系完美融合。当青云宗遭魔门围攻，他以程序员思维重构护宗大阵，意外激活上古禁制，揭露修真界覆灭危机。随着修为精进，李凡发现自己的穿越并非偶然，一场惊天阴谋浮出水面。他将代码与阵法结合，游历天下收集上古阵纹，解构天地法则，最终踏上拯救修真界的道路。

    第1章 车祸穿越
    雨点砸在头盔上，发出噼里啪啦的声响。李凡抹了一把脸上的雨水，低头看了眼手机上的订单倒计时，还有最后三分钟。
    "这鬼天气。"他咬紧牙关，将小电驴的油门拧到底。雨帘中，前方的红绿灯若隐若现，突然，一辆黑色轿车从右侧路口疾驰而出。
    刺耳的刹车声划破雨夜，李凡只觉得眼前一黑，整个人被巨大的冲击力抛向半空。世界在旋转，意识渐渐模糊，耳边只剩下雨水拍打地面的声音
    ...

    第2章 藏书阁的秘密
    慕容雪的目光在阵法与李凡之间来回游移。这个破损的除尘阵法，已经足足一个月无人问津了。即便是内门弟子，面对如此复杂的阵纹也要花费数日才能修复。而眼前这个杂役弟子，竟然只用了片刻功夫。
    "你是如何做到的？"她上前一步，声音里带着一丝自己都未曾察觉的急切。
    李凡下意识后退，手中的扫帚微微颤抖："我...我只是随便试试。"
    ...
    ```
5. **执行翻译任务**
    ```
    python run.py "path_to_txt_file" "target_language"
    ```
    您可以参考这个例子：
    ```
    python run.py "代码修仙.txt" "english"
    ```
    翻译好的文本会被输出到`global_config.json`里配置的`output_directory`目录里。