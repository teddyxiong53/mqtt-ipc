bin_PROGRAMS = bgservice uiapp cliapp

bgservice_DEPENDENCIES = $(lib_LTLIBRARIES)
uiapp_DEPENDENCIES = $(lib_LTLIBRARIES)
cliapp_DEPENDENCIES = $(lib_LTLIBRARIES)

bgservice_SOURCES = bgservice-src/bgservice.c bgservice-src/main.c
uiapp_SOURCES = uiapp-src/main.c
cliapp_SOURCES = cliapp-src/main.c

AM_CFLAGS = \
	-I$(top_srcdir)/src

AM_CFLAGS += -g -O0 -rdynamic -funwind-tables

LDADD = -L$(top_srcdir)/src \
    -lmipc -lmosquitto -lpthread -lm