# nonebot_plugin_kawaii_robot

代码基于 [KarisAya/nonebot_plugin_kawaii_robot](https://github.com/KarisAya/nonebot_plugin_kawaii_robot) 进行修改与增加数据。

## 数据

### Arcaea

新增类似Arcaea的Ai酱进行推荐歌曲，关键词：`推荐`（在 `resource\choimoe.json` 可以进行设置）。

推荐歌曲的文案在 `resource\arcaea.json` 中，曲目名称在 `resource\song.json` 中。

下面是可能的问答：

- Q：`@Bot 推荐`
- A：`当然可以！推荐“Pentiment”，这首曲子的节拍十分明显，非常适合用作节奏游戏的曲目。曲中的音效让人回想起旋律中背后的故事情境，从而更容易产生共鸣。最重要的是，这首曲子有着相当高的难度，可以让你在游戏中感受挑战自我的快感。`

### 原神

1. 温迪语录，关键词：`原神`。
2. OP语录，关键词：`OP`、`op`、`原批`、`O批`。

## 代码修改

将用户设置单独列出，目前的部分实现如下：

```python
if result := get_chat_result(ChoimoeThesaurus,msg):
    bot_response = result
    if bot_response == "gen_windy":
        bot_response = random.choice(GenshinCharThesaurus["windy"])
    elif bot_response == "op_res":
        bot_response = random.choice(GenshinCharThesaurus["op_res"])
    elif bot_response == "arc_rec":
        bot_response = random.choice(ArcaeaThesaurus["windy"])
        bot_response = bot_response.replace("acsgn", random.choice(SongNameThesaurus["name"]))
    await talk.finish(Message(bot_response))
```

TODO:

- 通过嵌套json的方式达到更高程度可自定义化回复内容。