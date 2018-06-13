wget -N https://s3.ap-northeast-2.amazonaws.com/earlybird2018/movie_titles.csv -P dataset

wget -N https://s3.ap-northeast-2.amazonaws.com/earlybird2018/original/train.csv -P dataset/original
wget -N https://s3.ap-northeast-2.amazonaws.com/earlybird2018/original/quiz.csv -P dataset/original
wget -N https://s3.ap-northeast-2.amazonaws.com/earlybird2018/original/quiz_answer.csv -P dataset/original

wget -N https://s3.ap-northeast-2.amazonaws.com/earlybird2018/small/train.csv -P dataset/small
wget -N https://s3.ap-northeast-2.amazonaws.com/earlybird2018/small/quiz_small.csv -P dataset/small
wget -N https://s3.ap-northeast-2.amazonaws.com/earlybird2018/small/quiz_small_answer.csv -P dataset/small
