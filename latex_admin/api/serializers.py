# Copyright © 2020 Murad Bashirov <carlsonmu@gmail.com>.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License

from rest_framework import serializers

from .models import File, Folder, Template


class FolderSerializer(serializers.ModelSerializer):
    """Serializer definition for model :model:`api.Folder`."""

    class Meta:
        """Meta class definition for serializer ``FolderSerializer``."""

        model = Folder
        fields = ['id', 'name', 'file_set']


class TemplateSerializer(serializers.ModelSerializer):
    """Serializer definition for model :model:`api.Template`."""

    files_in_root_dir = serializers.ListField(source="get_files_in_root")

    class Meta:
        """Meta class definiton for ``TemplateSerializer``."""

        model = Template
        fields = ['name', 'folder_set', 'files_in_root_dir']


class FileSerializer(serializers.ModelSerializer):
    """Serializer definiton for model :model:`api.File`."""

    class Meta:
        """Meta class definition for serializer ``FileSerializer``."""

        model = File
        fields = ['id', 'name', 'file_type', 'content']
