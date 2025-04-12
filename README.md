# AIWNT Core

[中文](./README.zh.md) | [日语](./README.ja.md)

![logo](./img/logo.webp)  

AIWNT (AI Web Novel Translator) is a tool specifically designed for translating ultra-long web novels consisting of tens of millions of characters. By utilizing the latest large language model technology, it aims to remove barriers to cross-language dissemination of web novels, enabling readers worldwide to enjoy their favorite works without boundaries.  

This project is a locally deployable open-source version built on a simple AI agent. It is a streamlined implementation of our [online workflow (aiwnt.com)](https://www.aiwnt.com/), yet it retains core functionalities. This allows users to deploy and use AIWNT in their own environments for efficient and flexible translation operations.  

## Features

- **High-Quality Translation Results**: Based on large language models, the quality of translations significantly surpasses traditional machine translation.
- **Efficient Processing Capabilities**: Optimized for handling ultra-long texts, it can swiftly translate content of tens of millions of characters.
- **User-Friendly**: With no complex deployment process, you can start translating with just one line of code.
- **Local Deployment**: Allows for personalized customization according to user needs, meeting specific requirements.

## Getting Started

If you prefer not to deploy it yourself, you can also try our more powerful [online workflow](https://www.aiwnt.com/). The online workflow offers higher translation quality and more stable service.  

Follow these steps to quickly embark on your AIWNT journey:  

### Prerequisites

- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [OpenAI API Key](https://platform.openai.com/account/api-keys)

### Step-by-Step Guide

1. **Clone the Repository**
    ```
    git clone https://github.com/Karasukaigan/aiwnt-core.git
    ```
2. **Install the OpenAI Library**
    ```
    pip install openai
    ```
3. **Configure global_config.json**  
    Remove the `.example` suffix from `global_config.json.example`, then edit `global_config.json` to include your actual API Key under `api_key`: 

    ```
    {
        "file_paths": {
            "output_directory": "output"
        },
        "api_config": {
            "base_url": "https://api.openai.com/v1",
            "api_key": "your_api_key_here",
            "model": "gpt-4o"
        }
    }
    ```
4. **Prepare a TXT File Like This**
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
5. **Execute Translation Tasks**
    ```
    python run.py "path_to_txt_file" "target_language"
    ```
   Here's an example:
    ```
    python run.py "代码修仙.txt" "english"
    ```
    The translated text will be output to the `output_directory` specified in the `global_config.json` configuration.