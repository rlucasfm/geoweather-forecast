from apscheduler.schedulers.background import BackgroundScheduler
from . import forecastApi


def starter():
    scheduler = BackgroundScheduler()
    scheduler.add_job(forecastApi.atualizar_forecast, 'interval', minutes=15)
    scheduler.start()