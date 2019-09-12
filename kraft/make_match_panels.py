from os.path import isfile, join

from pandas import read_csv

from .establish_path import establish_path
from .make_match_panel import make_match_panel
from .normalize_file_name import normalize_file_name


def make_match_panels(
    target_x_sample,
    data_dicts,
    drop_negative_target=False,
    directory_path=None,
    read_score_moe_p_value_fdr=False,
    **make_match_panel_keyword_arguments,
):

    for target_name, target in target_x_sample.iterrows():

        if drop_negative_target:

            target = target[0 < target]

        for data_name, data_dict in data_dicts.items():

            print(
                "Making match panel with target {} and data {}...".format(
                    target_name, data_name
                )
            )

            score_moe_p_value_fdr = None

            if directory_path is None:

                file_path_prefix = None

            else:

                file_path_prefix = join(
                    directory_path,
                    normalize_file_name(target_name),
                    normalize_file_name(data_name),
                )

                establish_path(file_path_prefix, "file")

                score_moe_p_value_fdr_file_path = "{}.tsv".format(file_path_prefix)

                if (
                    isfile(score_moe_p_value_fdr_file_path)
                    and read_score_moe_p_value_fdr
                ):

                    print(
                        "Reading score_moe_p_value_fdr from {}...".format(
                            score_moe_p_value_fdr_file_path
                        )
                    )

                    score_moe_p_value_fdr = read_csv(
                        score_moe_p_value_fdr_file_path, sep="\t", index_col=0
                    )

            make_match_panel(
                target,
                data_dict["dataframe"],
                score_moe_p_value_fdr=score_moe_p_value_fdr,
                data_data_type=data_dict["data_type"],
                layout={"title": {"text": "{}<br>{}".format(target_name, data_name)}},
                file_path_prefix=file_path_prefix,
                **make_match_panel_keyword_arguments,
            )
