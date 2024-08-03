最活跃的股票列表抓取和分析项目目标：
1. 每日抓取交易最活跃的股票列表里面的前 20 只股票及其相关的数据。链接:https://www.tradingview.com/markets/stocks-usa/market-movers-active/
2. 用 PostgreSQL 数据库存储抓取的数据。设计一个数据表 table 存储其中的股票代号 symbol, change%, Rel Volume, P/E 这几个数据。
3. 用 Flask框架开发这个应用,开个一个页面用来展示每天抓取的这些前 20 名股票的上面提到的几个数据。
4. 开发一个页面统计过去一段时间内，上榜的股票的出现次数排名。比如：过去五天/十天/20天 出现次数最高前 20 只的股票

sudo lsof -i :5432
sudo pkill -u postgres
