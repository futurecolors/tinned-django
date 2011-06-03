# -*- coding: utf-8 -*-
from django.shortcuts import render


def maintenance(request):
    return render(request, 'maintenance/maintenance.html', status=503)