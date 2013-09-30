#!/usr/bin/env python2.7

import os
import ConfigParser

import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

from plyer import notification

__version__ = '0.1'


def alert(dt=0, double_ding=False):
    SoundLoader.load('media/ding.wav').play()
    if double_ding:
        Clock.schedule_once(alert, 0.35)


def play_tick(dt=0):
    SoundLoader.load('media/tick.wav').play()


class ImmersionCoffeeTimer(BoxLayout):
    timer_display = ObjectProperty(None)
    rest_timer = ObjectProperty(None)
    stir_timer = ObjectProperty(None)
    total_timer = ObjectProperty(None)
    current_timer = NumericProperty(0)
    stir_time = NumericProperty(0)
    rest_time = NumericProperty(0)
    total_time = NumericProperty(0)
    timer_is_running = False
    timer_is_paused = False

    def __init__(self, **kwargs):
        super(ImmersionCoffeeTimer, self).__init__(**kwargs)
        self.app = App.get_running_app()
        config = self.app.read_config()
        self.stir_time = config.getint('timer', 'stir_after')
        self.rest_time = config.getint('timer', 'rest_for')
        self.total_time = self.stir_time + self.rest_time

    def start_pause_resume_timer(self):
        if self.timer_is_running:
            self.pause_timer()
        else:
            if self.timer_is_paused:
                self.resume_timer()
            else:
                self.start_timer()

    def start_timer(self):
        if not self.timer_is_running:
            self.current_timer = self.stir_time + self.rest_time
            self.timer_display.text = self.format_timer(self.current_timer)
            Clock.schedule_interval(self._decrement_timer, 1)
            Clock.schedule_once(self._stir_notification, self.stir_time)
            self.timer_is_running = True
            self.start_pause_resume_button.text = "Pause Timer"

    def pause_timer(self):
        if self.timer_is_running:
            self.timer_is_running = False
            self.timer_is_paused = True
            Clock.unschedule(self._decrement_timer)
            Clock.unschedule(self._stir_notification)
            self.app.write_config(pause=self.current_timer)
            self.start_pause_resume_button.text = "Resume Timer"

    def resume_timer(self):
        if not self.timer_is_running:
            config = self.app.read_config()
            self.current_timer = config.getint('timer', 'paused_at')
            self.clock_tick = Clock.schedule_interval(self._decrement_timer, 1)
            if self.current_timer > self.stir_time:
                self.clock_stir = Clock.schedule_once(self._stir_notification,
                                                      self.current_timer - self.stir_time)
            self.timer_is_running = True
            self.timer_is_paused = False
            self.start_pause_resume_button.text = "Pause Timer"

    def _decrement_timer(self, dt):
        play_tick()
        if self.current_timer > 1:
            self.current_timer -= 1
            return True
        else:
            self._finish_timer()
            return False

    def _finish_timer(self):
        self.timer_is_running = False
        notification.notify("Immersion Coffee Timer", "Coffee is ready.")
        self.timer_display.text = "Done"
        alert(double_ding=True)
        self.start_pause_resume_button.text = "Start Timer"

    def format_timer(self, sec):
        minutes, seconds = divmod(sec, 60)
        if seconds < 10:
            seconds = "0{}".format(seconds)
        return "{}:{}".format(minutes, seconds)

    def parse_timer(self, ftimer):
        minutes, seconds = ftimer.split(':')
        return (int(minutes)*60)+int(seconds)

    def _update_timers(self):
        self.stir_time = self.parse_timer(self.stir_timer.text)
        self.rest_time = self.parse_timer(self.rest_timer.text)
        self.total_time = self.stir_time + self.rest_time
        self.app.write_config(self.stir_time, self.rest_time)

    def _stir_notification(self, dt):
        notification.notify("Immersion Coffee Timer", "Time to stir the coffee.")
        alert()

    def cancel_timer(self):
        self.timer_is_running = False
        self.timer_is_paused = False
        Clock.unschedule(self._decrement_timer)
        Clock.unschedule(self._stir_notification)
        self.current_timer = 0
        self.start_pause_resume_button.text = "Start Timer"


class ImmersionCoffeeTimerApp(App):

    default_stir_time = 90
    default_rest_time = 240
    config_file_name = 'config.ini'

    def __init__(self, **kwargs):
        super(ImmersionCoffeeTimerApp, self).__init__(**kwargs)
        self.config_file = os.path.join(self.user_data_dir,
                                        self.config_file_name)

    def read_config(self):
        config = ConfigParser.SafeConfigParser()
        if os.path.isfile(self.config_file):
            config.read(self.config_file)
        else:
            config = self.write_config(self.default_stir_time,
                                       self.default_rest_time)
        return config

    def write_config(self, stir=0, rest=0, pause=0):
        config = ConfigParser.SafeConfigParser()
        config.add_section('timer')
        config.set('timer', 'stir_after', str(stir))
        config.set('timer', 'rest_for', str(rest))
        config.set('timer', 'paused_at', str(pause))
        with open(self.config_file, 'wb') as cf:
            config.write(cf)
        return config

    def build(self):
        config = self.read_config()
        return ImmersionCoffeeTimer()

    def on_pause(self):
        return True

    def on_resume(self):
        pass


if __name__ == '__main__':
    app = ImmersionCoffeeTimerApp()
    app.run()
