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

from rest_framework import viewsets

from .models import File, Folder, Template
from .serializers import FileSerializer, FolderSerializer, TemplateSerializer


class FolderViewSet(viewsets.ReadOnlyModelViewSet):
    """This viewset automatically provides `list` and `retrieve` actions."""

    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class TemplateViewSet(viewsets.ReadOnlyModelViewSet):
    """This viewset automatically provides `list` and `retrieve` actions."""

    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class FileViewSet(viewsets.ReadOnlyModelViewSet):
    """This viewset automatically provides `list` and `retrieve` actions."""

    queryset = File.objects.all()
    serializer_class = FileSerializer
