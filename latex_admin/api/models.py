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

from django.db import models


class Template(models.Model):
    """
    Template structure for latex-admin.

    Columns:
        name: name of the template.
    """

    name = models.CharField(max_length=155, unique=True)

    def __str__(self):
        return self.name

    def get_files_in_root(self) -> list:
        """Gets the files in root dir."""
        files_in_root = []
        files_in_folders = []
        for folder in self.folder_set.all():
            for _file in folder.file_set.all():
                files_in_folders.append(_file)
        for _file in self.file_set.all():
            if _file not in files_in_folders:
                files_in_root.append(_file.id)
        return files_in_root


class Folder(models.Model):
    """
    A folder in a template for latex-admin.

    Columns:
        name: name of the folder.
        template: the template that the folder belongs.
    """

    name = models.CharField(max_length=155)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class File(models.Model):
    """
    Template file for latex-admin.

    Columns:
        name: name of the file.
        content: the content of the file.
        file_type: type of the file, cchoices are sty, tex or cls.
    """

    name = models.CharField(max_length=155)
    content = models.TextField()
    STY = 'sty'
    TEX = 'tex'
    CLS = 'cls'
    TYPE_CHOICES = [
        (STY, 'package'),
        (CLS, 'class'),
        (TEX, 'ordinary .tex')
    ]
    file_type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        default=TEX,
    )
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)
    template = models.ForeignKey(Template, on_delete=models.CASCADE, null=True, blank=True)

    def get_full_name(self) -> str:
        """Returns the full name of file: template_{name}.{file_type}."""
        full_name = 'template_%s.%s' % (self.first_name, self.file_type)
        return full_name

    def __str__(self):
        return self.name
