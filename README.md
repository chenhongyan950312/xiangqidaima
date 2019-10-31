

下棋命令：

 - --ai_count 指定ai的个数，1是人机对战，2是看两个ai下棋
 - --ai_function 指定ai的下棋方法，是思考（mcts，会慢），还是直觉（net，下棋快）
 - --play_playout 指定ai进行MCTS的模拟次数
 - --delay和--end_delay默认就好，两个ai下棋太快，就不知道俩ai怎么下的了：）
 - --human_color 指定人类棋手的颜色，w是先手，b是后手

训练命令举例：

python main.py --mode train --train_playout 1200 --batch_size 512 --search_threads 16 --processor gpu --num_gpus 2 --res_block_nums 7

下棋命令举例：

python main.py --mode play --ai_count 1 --ai_function mcts --play_playout 1200 --human_color w

# 许可
Licensed under the MIT License with the [`996ICU License`](https://github.com/996icu/996.ICU/blob/master/LICENSE).
