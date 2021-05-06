#!/usr/bin/env python

import os
import shutil
import re

source_folder = 'C:\\photo_sample'
target_folder = 'C:\\photo_sample_new'

shutil.rmtree(target_folder, ignore_errors=True)
os.makedirs(target_folder, 0o777)
# os.chmod(target_folder, stat.S_IWRITE)
# for file in os.listdir(target_folder):
#     os.remove(target_folder + '\\' + file)

errors = []

print('Copy files from ' + source_folder + ' to ' + target_folder)
for src_name in os.listdir(source_folder):
    file_name_pattern = re.compile('IMG_(\\d{4})(\\d{2})(\\d{2})_(\\d{2})(\\d{2})(\\d{2})(_\\d+)?(\\.\\w+)')
    if file_name_pattern.match(src_name):
        dst_name = file_name_pattern.sub('\\1.\\2.\\3_\\4.\\5.\\6\\7\\8', src_name)

        # if len(src_name) > 23:
        #     dst_name = src_name[4:8] + '.' + src_name[8:10] + '.' + src_name[10:12] + '_' + src_name[13:15] + '.' \
        #                + src_name[15:17] + '.' + src_name[17:19] + '-' + src_name[20:21] + src_name[21:25]
        # else:
        #     dst_name = src_name[4:8] + '.' + src_name[8:10] + '.' + src_name[10:12] + '_' + src_name[13:15] + '.' \
        #                + src_name[15:17] + '.' + src_name[17:19] + src_name[19:23]

        shutil.copy(os.path.join(source_folder, src_name), os.path.join(target_folder, dst_name))
        # cmd = 'copy ' + os.path.join(source_folder, src_name) + ' ' + os.path.join(target_folder, dst_name)
        # print(cmd)
        # os.system(cmd)
        print(src_name + ' -> ' + dst_name)
    else:
        error = 'ERROR: cannot rename ' + src_name + ' file. File name pattern mismatch.'
        print(error)
        errors.append(error)

if len(errors) == 0:
    print('\nDone. Process finished successfully.')
else:
    print('\nDone. Process finished with errors. See log above.')