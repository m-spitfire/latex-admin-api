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

from django.contrib import admin

from .models import File, Folder, Template


class FileAdmin(admin.ModelAdmin):
    """Model admin definition for :model:`api.File` model. Needed for custom columns."""

    list_display = ('name', 'file_type', 'template', 'folder')


admin.site.register(Folder)
admin.site.register(Template)
admin.site.register(File, FileAdmin)
