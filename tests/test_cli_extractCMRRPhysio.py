import os

import tempfile
import filecmp

# get output_dir
tmp_dir = tempfile.gettempdir()
output_dir = tmp_dir


# get data_dir
file_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(file_dir, 'data')

# get matlab result dir
matlab_result_dir = os.path.join(data_dir, 'matlab_results')


def test_physio_data():
    '''test physio: physio.dcm'''

    cmd = f"extractCMRRPhysio {os.path.join(data_dir,'physio.dcm')} {output_dir}"

    # return 0 is no error
    r = os.system(cmd)

    # print(r)
    assert r == 0

    # test matlab results
    info_file = 'Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_Info.log'
    puls_file = 'Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_PULS.log'
    resp_file = 'Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_RESP.log'

    # filecmp.cmp return True if two files contents are same
    assert filecmp.cmp(os.path.join(matlab_result_dir, info_file),
                       os.path.join(output_dir, info_file))

    assert filecmp.cmp(os.path.join(matlab_result_dir, puls_file),
                       os.path.join(output_dir, puls_file))

    assert filecmp.cmp(os.path.join(matlab_result_dir, resp_file),
                       os.path.join(output_dir, resp_file))


#########
# test non-physio: non-physio.dcm
#########

# cli_test_physio:
#     extractCMRRPhysio ./data/test.dcm  ${OUTPUT_DIR}
#     # diff -u ${OUTPUT_DIR}/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_Info.log ./data/matlab_results/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_Info.log
#     diff - u ${OUTPUT_DIR}/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_PULS.log ./data/matlab_results/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_PULS.log
#     diff ${OUTPUT_DIR}/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_RESP.log ./data/matlab_results/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_RESP.log

#     # rm ${OUTPUT_DIR}/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_Info.log
#     # rm ${OUTPUT_DIR}/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_PULS.log
#     # rm ${OUTPUT_DIR}/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_RESP.log

# cli_test_non-physio:
#     extractCMRRPhysio ./data/test.dcm  ${OUTPUT_DIR}
