# coding=utf-8
from __future__ import unicode_literals, absolute_import

from filer.models import Folder
from rest_framework import serializers


class FilerFolderModelSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Folder
        fields = ('id', 'name')

    @staticmethod
    def get_name(obj):
        return obj.pretty_logical_path
