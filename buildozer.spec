[app]

# (str) Title of your application
title = Immersion Coffee Timer

# (str) Package name
package.name = immersioncoffeetimer

# (str) Package domain (needed for android/ios packaging)
package.domain = com.feralrooster

# (str) Source code where the main.py live
source.dir = ./immersioncoffeetimer

# (list) Source files to include (let empty to include all the files)
#source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = .komodoproject

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versionning (method 1)
version.regex = __version__ = '(.*)'
version.filename = %(source.dir)s/main.py

# (str) Application versionning (method 2)
# version = 1.2.0

# (list) Application requirements
requirements = kivy

# (str) Presplash of the application
presplash.filename = %(source.dir)s/media/loading-512.png

# (str) Icon of the application
icon.filename = %(source.dir)s/media/icon-48.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = all

# (bool) Indicate if the application should be fullscreen or not
fullscreen = True


#
# Android specific
#

# (list) Permissions
android.permissions = WAKE_LOCK

# (int) Android API to use
android.api = 14

# (int) Minimum API required (8 = Android 2.2 devices)
android.minapi = 8

# (int) Android SDK version to use
android.sdk = 21

# (str) Android NDK version to use
android.ndk = 8e

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path = 

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.renpy.android.PythonActivity

# (bool) Indicate whther to use private app file storage (True, default)
# or SD card storage (False)
android.private_storage = True

# (str) Semicolon separated list of Java .jar files to add to the libs so
# that pyjnius can access their classes. Don't add jars that you do not need,
# since extra jars can slow down the build process. Allows wildcards matching,
# for example: OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar;bar.jar;path/to/more/*.jar

# (str) python-for-android branch to use, if not master, useful to try
# not yet merged features.
#android.branch = master

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (bool) 
wakelock = True

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters = 


#
# iOS specific
#

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = %(ios.codesign.debug)s


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 1


# -----------------------------------------------------------------------------
# List as sections
# 
# You can define all the "list" as [section:key].
# Each line will be considered as a option to the list.
# Let's take [app] / source.exclude_patterns.
# Instead of doing:
#
#     [app]
#     source.exclude_patterns = license,data/audio/*.wav,data/images/original/*
#
# This can be translated into:
#
#     [app:source.exclude_patterns]
#     license
#     data/audio/*.wav
#     data/images/original/*
#


# -----------------------------------------------------------------------------
# Profiles
#
# You can extend section / key with a profile
# For example, you want to deploy a demo version of your application without
# HD content. You could first change the title to add "(demo)" in the name
# and extend the excluded directories to remove the HD content.
#
#     [app@demo]
#     title = My Application (demo)
#
#     [app:source.exclude_patterns@demo]
#     images/hd/*
#
# Then, invoke the command line with the "demo" profile:
#
#     buildozer --profile demo android debug
