from plotly.io import templates

from .add_conda_to_path import add_conda_to_path
from .ALMOST_ZERO import ALMOST_ZERO
from .apply_function_on_2_vectors import apply_function_on_2_vectors
from .apply_function_on_slices_from_2_dataframes import (
    apply_function_on_slices_from_2_dataframes,
)
from .apply_function_on_slices_from_2_matrices import (
    apply_function_on_slices_from_2_matrices,
)
from .BAD_VALUES import BAD_VALUES
from .call_function_with_multiprocess import call_function_with_multiprocess
from .cast_object_to_builtin import cast_object_to_builtin
from .check_array_for_bad import check_array_for_bad
from .clean_and_write_dataframe_to_tsv import clean_and_write_dataframe_to_tsv
from .clip_array_by_standard_deviation import clip_array_by_standard_deviation
from .cluster_clustering_x_element_and_compute_ccc import (
    cluster_clustering_x_element_and_compute_ccc,
)
from .cluster_matrix import cluster_matrix
from .compute_element_x_dimension_joint_probability import (
    compute_element_x_dimension_joint_probability,
)
from .compute_element_x_dimension_posterior_probability import (
    compute_element_x_dimension_posterior_probability,
)
from .compute_empirical_p_value import compute_empirical_p_value
from .compute_empirical_p_values_and_fdrs import compute_empirical_p_values_and_fdrs
from .compute_information_coefficient_between_2_vectors import (
    compute_information_coefficient_between_2_vectors,
)
from .compute_information_distance_between_2_vectors import (
    compute_information_distance_between_2_vectors,
)
from .compute_kullback_leibler_divergence import compute_kullback_leibler_divergence
from .compute_matrix_norm import compute_matrix_norm
from .compute_normal_pdf_margin_of_error import compute_normal_pdf_margin_of_error
from .compute_vector_bandwidth import compute_vector_bandwidth
from .compute_vector_context import compute_vector_context
from .compute_vector_entropy import compute_vector_entropy
from .correlate_2_vectors import correlate_2_vectors
from .count_gene_impacts_from_variant_dicts import count_gene_impacts_from_variant_dicts
from .DATA_DIRECTORY_PATH import DATA_DIRECTORY_PATH
from .download_and_parse_geo import download_and_parse_geo
from .download_url import download_url
from .download_url_and_extract import download_url_and_extract
from .drop_dataframe_slice import drop_dataframe_slice
from .drop_dataframe_slice_greedily import drop_dataframe_slice_greedily
from .echo_or_print_str import echo_or_print_str
from .establish_path import establish_path
from .estimate_element_x_dimension_kernel_density import (
    estimate_element_x_dimension_kernel_density,
)
from .exit_ import exit_
from .fit_each_dataframe_row_to_skew_t_pdf import fit_each_dataframe_row_to_skew_t_pdf
from .fit_vector_to_skew_t_pdf import fit_vector_to_skew_t_pdf
from .flatten_nested_iterable import flatten_nested_iterable
from .FRACTION_GRID_EXTENSION import FRACTION_GRID_EXTENSION
from .get_child_paths import get_child_paths
from .get_chromosome_size_from_fasta_gz import get_chromosome_size_from_fasta_gz
from .get_colormap_colors import get_colormap_colors
from .get_conda_environments import get_conda_environments
from .get_conda_prefix import get_conda_prefix
from .get_data_type import get_data_type
from .get_dataframe_slice_fraction_good import get_dataframe_slice_fraction_good
from .get_gff3_attribute import get_gff3_attribute
from .get_git_versions import get_git_versions
from .get_intersections_between_2_vectors import get_intersections_between_2_vectors
from .get_machine import get_machine
from .get_mesh_grid_point_x_dimension_d_dimensions import (
    get_mesh_grid_point_x_dimension_d_dimensions,
)
from .get_sequence_from_fasta_or_fasta_gz import get_sequence_from_fasta_or_fasta_gz
from .get_shell_environment import get_shell_environment
from .get_triangulation_edges_from_point_x_dimension import (
    get_triangulation_edges_from_point_x_dimension,
)
from .get_variant_start_and_end_positions import get_variant_start_and_end_positions
from .get_variants_from_vcf_or_vcf_gz import get_variants_from_vcf_or_vcf_gz
from .get_vcf_genotype import get_vcf_genotype
from .get_vcf_info import get_vcf_info
from .get_vcf_info_ann import get_vcf_info_ann
from .get_vcf_sample_format import get_vcf_sample_format
from .GPSMap import GPSMap
from .group_and_apply_function_on_each_group_in_iterable import (
    group_and_apply_function_on_each_group_in_iterable,
)
from .hierarchical_consensus_cluster_dataframe import (
    hierarchical_consensus_cluster_dataframe,
)
from .hierarchical_consensus_cluster_dataframe_with_ks import (
    hierarchical_consensus_cluster_dataframe_with_ks,
)
from .infer import infer
from .infer_assuming_independence import infer_assuming_independence
from .initialize_logger import initialize_logger
from .install_and_activate_conda import install_and_activate_conda
from .install_python_libraries import install_python_libraries
from .is_conda_directory_path import is_conda_directory_path
from .is_in_git_repository import is_in_git_repository
from .is_program import is_program
from .is_sorted_array import is_sorted_array
from .is_str_version import is_str_version
from .log_and_return_response import log_and_return_response
from .log_array import log_array
from .make_binary_dataframe_from_categorical_series import (
    make_binary_dataframe_from_categorical_series,
)
from .make_colorscale_from_colors import make_colorscale_from_colors
from .make_context_matrix import make_context_matrix
from .make_gitkeep import make_gitkeep
from .make_match_panel import make_match_panel
from .make_match_panel_annotations import make_match_panel_annotations
from .make_match_panel_summary import make_match_panel_summary
from .make_match_panels import make_match_panels
from .make_mesh_grid_point_x_dimension import make_mesh_grid_point_x_dimension
from .make_reflecting_grid import make_reflecting_grid
from .make_variant_dict_consistent import make_variant_dict_consistent
from .make_variant_dict_from_vcf_row import make_variant_dict_from_vcf_row
from .make_variant_n_from_vcf_file_path import make_variant_n_from_vcf_file_path
from .make_variant_n_from_vcf_row import make_variant_n_from_vcf_row
from .make_vector_grid import make_vector_grid
from .map_objects_to_ints import map_objects_to_ints
from .merge_2_dicts_with_function import merge_2_dicts_with_function
from .mf_by_multiple_v_and_h import mf_by_multiple_v_and_h
from .mf_by_multiplicative_update import mf_by_multiplicative_update
from .mf_consensus_cluster_dataframe import mf_consensus_cluster_dataframe
from .mf_consensus_cluster_dataframe_with_ks import (
    mf_consensus_cluster_dataframe_with_ks,
)
from .N_GRID import N_GRID
from .nmf_by_sklearn import nmf_by_sklearn
from .NONE_STRS import NONE_STRS
from .normalize_array import normalize_array
from .normalize_cell_line_names import normalize_cell_line_names
from .normalize_contig import normalize_contig
from .normalize_file_name import normalize_file_name
from .normalize_git_url import normalize_git_url
from .normalize_path import normalize_path
from .normalize_series_or_dataframe import normalize_series_or_dataframe
from .pick_colors import pick_colors
from .plot_bayesian_nomogram import plot_bayesian_nomogram
from .plot_bubble_map import plot_bubble_map
from .plot_context import plot_context
from .plot_heat_map import plot_heat_map
from .plot_histogram import plot_histogram
from .plot_mesh_grid import plot_mesh_grid
from .plot_plotly_figure import plot_plotly_figure
from .plot_scatter_and_annotate import plot_scatter_and_annotate
from .print_function_information import print_function_information
from .print_header_in_terminal import print_header_in_terminal
from .process_feature_x_sample import process_feature_x_sample
from .RANDOM_SEED import RANDOM_SEED
from .read_gff3 import read_gff3
from .read_gmt import read_gmt
from .read_gps_map import read_gps_map
from .read_json import read_json
from .read_process_write_gene_x_cell import read_process_write_gene_x_cell
from .read_where_and_map_column_name_on_hdf5_table import (
    read_where_and_map_column_name_on_hdf5_table,
)
from .remove_path import remove_path
from .rescale_x_y_coordiantes_in_polar_coordiante import (
    rescale_x_y_coordiantes_in_polar_coordiante,
)
from .run_command import run_command
from .sample_from_each_series_value import sample_from_each_series_value
from .scale_point_x_dimension_dimension import scale_point_x_dimension_dimension
from .select_and_group_feature_x_tcga_sample_by_sample_type import (
    select_and_group_feature_x_tcga_sample_by_sample_type,
)
from .select_gene_symbol import select_gene_symbol
from .select_series_indices import select_series_indices
from .separate_information_x_sample import separate_information_x_sample
from .shuffle_each_matrix_slice import shuffle_each_matrix_slice
from .skip_quote_and_split_str import skip_quote_and_split_str
from .solve_ax_equal_b import solve_ax_equal_b
from .solve_for_h import solve_for_h
from .split_codons import split_codons
from .split_dataframe import split_dataframe
from .summarize_feature_x_sample import summarize_feature_x_sample
from .title_str import title_str
from .train_and_classify import train_and_classify
from .train_and_regress import train_and_regress
from .unmesh import unmesh
from .untitle_str import untitle_str
from .update_h_by_multiplicative_update import update_h_by_multiplicative_update
from .update_variant_dict import update_variant_dict
from .update_w_by_multiplicative_update import update_w_by_multiplicative_update
from .VCF_ANN_KEYS import VCF_ANN_KEYS
from .VCF_COLUMNS import VCF_COLUMNS
from .write_gps_map import write_gps_map
from .write_json import write_json

templates.default = "plotly_white"
