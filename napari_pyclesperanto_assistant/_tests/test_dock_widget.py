# from napari_pyclesperanto_assistant import napari_experimental_provide_dock_widget

# add your tests here...
def test_whatever():
    pass

import pytest

@pytest.fixture
def make_test_viewer(qtbot, request):
    from napari import Viewer
    viewers = []

    def actual_factory(*model_args, viewer_class=Viewer, **model_kwargs):
        model_kwargs.setdefault('show', False)
        viewer = viewer_class(*model_args, **model_kwargs)
        viewers.append(viewer)
        return viewer

    yield actual_factory

    for viewer in viewers:
        viewer.close()


def test_whatever2(make_test_viewer):
    import napari
    viewer = make_test_viewer()
    pass

def test_whatever3():
    import napari
    viewer = napari.Viewer(show=False)

    import napari_pyclesperanto_assistant
    assistant_gui = napari_pyclesperanto_assistant.napari_plugin(viewer)
    pass


def test_complex_workflow():
    print("x")

    import napari
    import napari_pyclesperanto_assistant
    from pathlib import Path
    print("7")

    root = Path(napari_pyclesperanto_assistant.__file__).parent

    filename = str(root / 'data' / 'Lund_000500_resampled-cropped.tif')
    # filename = str(root / 'data' / 'CalibZAPWfixed_000154_max-16.tif')

    # create Qt GUI context
    print("a")
    napari.gui_qt()

    # start napari
    print("b")
    viewer = napari.Viewer(show=False)

    print("c")
    layer = viewer.open(filename)
    layer[0].metadata['filename'] = filename

    # attach the assistant
    print("d")
    assistant_gui = napari_pyclesperanto_assistant.napari_plugin(viewer)

    print("e")
    from .._operations._operations import denoise, background_removal, filter, binarize, combine, label, \
        label_processing, map, mesh, measure, label_measurements, transform, projection
    assistant_gui._activate(denoise)
    print("f")
    assistant_gui._activate(background_removal)
    assistant_gui._activate(filter)
    assistant_gui._activate(binarize)

    print("g")
    viewer.close()
