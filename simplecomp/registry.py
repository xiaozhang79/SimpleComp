from lmms_eval.models.registry_v2 import ModelManifest


def get_manifests() -> list[ModelManifest]:
    return [
        ModelManifest(
            model_id="llava_onevision_simplecomp",
            simple_class_path="simplecomp.llava_onevision.LlavaOneVisionSimpleComp",
        ),
        ModelManifest(
            model_id="llava_video_simplecomp",
            simple_class_path="simplecomp.llava_video.LlavaVideoSimpleComp",
        ),
        ModelManifest(
            model_id="internvl3_simplecomp",
            simple_class_path="simplecomp.internvl3.InternVL3SimpleComp",
        ),
    ]
