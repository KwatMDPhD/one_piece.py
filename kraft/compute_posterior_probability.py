from numpy import apply_along_axis

from .compute_joint_probability import compute_joint_probability
from .get_d_dimensions import get_d_dimensions
from .plot_mesh_grid import plot_mesh_grid
from .unmesh import unmesh


def compute_posterior_probability(
    observation_x_dimension,
    plot=True,
    dimension_names=None,
    **estimate_kernel_density_keyword_arguments,
):

    mesh_grid_point_x_dimension, mesh_grid_point_joint_probability = compute_joint_probability(
        observation_x_dimension,
        plot=plot,
        dimension_names=dimension_names,
        **estimate_kernel_density_keyword_arguments,
    )

    d_target_dimension = get_d_dimensions(mesh_grid_point_x_dimension)[-1]

    joint_probability = unmesh(
        mesh_grid_point_x_dimension, mesh_grid_point_joint_probability
    )[1]

    mesh_grid_point_posterior_probability = apply_along_axis(
        lambda _1d_array: _1d_array / (_1d_array.sum() * d_target_dimension),
        -1,
        joint_probability,
    ).reshape(mesh_grid_point_joint_probability.shape)

    if plot:

        plot_mesh_grid(
            mesh_grid_point_x_dimension,
            mesh_grid_point_posterior_probability,
            title="Posterior Probability",
            dimension_names=dimension_names,
        )

    return mesh_grid_point_x_dimension, mesh_grid_point_posterior_probability
