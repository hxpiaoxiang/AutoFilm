#!/usr/bin/env python3
# encoding: utf-8

from asyncio import get_event_loop
from sys import path
from os.path import dirname
path.append(dirname(dirname(__file__)))

# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from apscheduler.triggers.cron import CronTrigger

from app.core import settings
from app.extensions import LOGO
from app.modules import Alist2Strm, Ani2Alist


if __name__ == "__main__":
    print(LOGO + str(settings.APP_VERSION).center(65, "="))
    print(f"AutoFilm {settings.APP_VERSION}启动中...")

    # scheduler = AsyncIOScheduler()
    
    if settings.AlistServerList:
        print("检测到Alist2Strm模块配置，正在执行")
        for server in settings.AlistServerList:
            # cron = server.get("cron")
            # if cron:
            #     scheduler.add_job(Alist2Strm(**server).run,trigger=CronTrigger.from_crontab(cron))
            #     print(f"{server["id"]}已被添加至后台任务")
            # else:
            #     print(f"{server["id"]}未设置Cron")
            Alist2Strm(**server)
    else:
        print("未检测到Alist2Strm模块配置")

    # if settings.Ani2AlistList:
    #     print("检测到Ani2Alist模块配置，正在添加至后台任务")
    #     for server in settings.Ani2AlistList:
    #         cron = server.get("cron")
    #         if cron:
    #             scheduler.add_job(Ani2Alist(**server).run,trigger=CronTrigger.from_crontab(cron))
    #             print(f"{server["id"]}已被添加至后台任务")
    #         else:
    #             print(f"{server["id"]}未设置Cron")
    # else:
    #     print("未检测到Ani2Alist模块配置")

    # scheduler.start()

    # try:
    #     get_event_loop().run_forever()
    # except (KeyboardInterrupt, SystemExit):
    #     print("AutoFilm程序退出！")
