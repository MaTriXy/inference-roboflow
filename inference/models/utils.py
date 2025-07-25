import warnings

from inference.core.env import (
    API_KEY,
    CORE_MODEL_CLIP_ENABLED,
    CORE_MODEL_DOCTR_ENABLED,
    CORE_MODEL_GAZE_ENABLED,
    CORE_MODEL_GROUNDINGDINO_ENABLED,
    CORE_MODEL_OWLV2_ENABLED,
    CORE_MODEL_PE_ENABLED,
    CORE_MODEL_SAM2_ENABLED,
    CORE_MODEL_SAM_ENABLED,
    CORE_MODEL_TROCR_ENABLED,
    CORE_MODEL_YOLO_WORLD_ENABLED,
    DEPTH_ESTIMATION_ENABLED,
    FLORENCE2_ENABLED,
    MOONDREAM2_ENABLED,
    PALIGEMMA_ENABLED,
    QWEN_2_5_ENABLED,
    SMOLVLM2_ENABLED,
)
from inference.core.models.base import Model
from inference.core.models.stubs import (
    ClassificationModelStub,
    InstanceSegmentationModelStub,
    KeypointsDetectionModelStub,
    ObjectDetectionModelStub,
)
from inference.core.registries.roboflow import get_model_type
from inference.core.warnings import ModelDependencyMissing
from inference.models import (
    YOLACT,
    ResNetClassification,
    RFDETRObjectDetection,
    VitClassification,
    YOLONASObjectDetection,
    YOLOv5InstanceSegmentation,
    YOLOv5ObjectDetection,
    YOLOv7InstanceSegmentation,
    YOLOv8Classification,
    YOLOv8InstanceSegmentation,
    YOLOv8ObjectDetection,
    YOLOv9ObjectDetection,
    YOLOv10ObjectDetection,
    YOLOv11InstanceSegmentation,
    YOLOv11ObjectDetection,
    YOLOv12ObjectDetection,
)
from inference.models.yolov8.yolov8_keypoints_detection import YOLOv8KeypointsDetection
from inference.models.yolov11.yolov11_keypoints_detection import (
    YOLOv11KeypointsDetection,
)

ROBOFLOW_MODEL_TYPES = {
    ("classification", "stub"): ClassificationModelStub,
    ("classification", "vit"): VitClassification,
    ("classification", "resnet18"): ResNetClassification,
    ("classification", "resnet34"): ResNetClassification,
    ("classification", "resnet50"): ResNetClassification,
    ("classification", "resnet101"): ResNetClassification,
    ("classification", "yolov8"): YOLOv8Classification,
    ("classification", "yolov8n"): YOLOv8Classification,
    ("classification", "yolov8s"): YOLOv8Classification,
    ("classification", "yolov8m"): YOLOv8Classification,
    ("classification", "yolov8l"): YOLOv8Classification,
    ("classification", "yolov8x"): YOLOv8Classification,
    ("object-detection", "stub"): ObjectDetectionModelStub,
    ("object-detection", "yolov5"): YOLOv5ObjectDetection,
    ("object-detection", "yolov5v2s"): YOLOv5ObjectDetection,
    ("object-detection", "yolov5v6n"): YOLOv5ObjectDetection,
    ("object-detection", "yolov5v6s"): YOLOv5ObjectDetection,
    ("object-detection", "yolov5v6m"): YOLOv5ObjectDetection,
    ("object-detection", "yolov5v6l"): YOLOv5ObjectDetection,
    ("object-detection", "yolov5v6x"): YOLOv5ObjectDetection,
    ("object-detection", "yolov9"): YOLOv9ObjectDetection,
    ("object-detection", "yolov8"): YOLOv8ObjectDetection,
    ("object-detection", "yolov8s"): YOLOv8ObjectDetection,
    ("object-detection", "yolov8n"): YOLOv8ObjectDetection,
    ("object-detection", "yolov8s"): YOLOv8ObjectDetection,
    ("object-detection", "yolov8m"): YOLOv8ObjectDetection,
    ("object-detection", "yolov8l"): YOLOv8ObjectDetection,
    ("object-detection", "yolov8x"): YOLOv8ObjectDetection,
    ("object-detection", "yolo_nas_s"): YOLONASObjectDetection,
    ("object-detection", "yolo_nas_m"): YOLONASObjectDetection,
    ("object-detection", "yolo_nas_l"): YOLONASObjectDetection,
    ("object-detection", "yolov10"): YOLOv10ObjectDetection,
    ("object-detection", "yolov10s"): YOLOv10ObjectDetection,
    ("object-detection", "yolov10n"): YOLOv10ObjectDetection,
    ("object-detection", "yolov10b"): YOLOv10ObjectDetection,
    ("object-detection", "yolov10m"): YOLOv10ObjectDetection,
    ("object-detection", "yolov10l"): YOLOv10ObjectDetection,
    ("object-detection", "yolov10x"): YOLOv10ObjectDetection,
    ("object-detection", "yolov11"): YOLOv11ObjectDetection,
    ("object-detection", "yolov11s"): YOLOv11ObjectDetection,
    ("object-detection", "yolov11n"): YOLOv11ObjectDetection,
    ("object-detection", "yolov11b"): YOLOv11ObjectDetection,
    ("object-detection", "yolov11m"): YOLOv11ObjectDetection,
    ("object-detection", "yolov11l"): YOLOv11ObjectDetection,
    ("object-detection", "yolov11x"): YOLOv11ObjectDetection,
    ("object-detection", "yolov12"): YOLOv12ObjectDetection,
    ("object-detection", "yolov12s"): YOLOv12ObjectDetection,
    ("object-detection", "yolov12n"): YOLOv12ObjectDetection,
    ("object-detection", "yolov12m"): YOLOv12ObjectDetection,
    ("object-detection", "yolov12l"): YOLOv12ObjectDetection,
    ("object-detection", "yolov12x"): YOLOv12ObjectDetection,
    ("object-detection", "rfdetr-base"): RFDETRObjectDetection,
    ("object-detection", "rfdetr-large"): RFDETRObjectDetection,
    (
        "instance-segmentation",
        "yolov11n",
    ): YOLOv11InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov11s",
    ): YOLOv11InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov11m",
    ): YOLOv11InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov11l",
    ): YOLOv11InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov11x",
    ): YOLOv11InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov11n-seg",
    ): YOLOv11InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov11s-seg",
    ): YOLOv11InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov11m-seg",
    ): YOLOv11InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov11l-seg",
    ): YOLOv11InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov11x-seg",
    ): YOLOv11InstanceSegmentation,
    ("keypoint-detection", "yolov11n"): YOLOv11KeypointsDetection,
    ("keypoint-detection", "yolov11s"): YOLOv11KeypointsDetection,
    ("keypoint-detection", "yolov11m"): YOLOv11KeypointsDetection,
    ("keypoint-detection", "yolov11l"): YOLOv11KeypointsDetection,
    ("keypoint-detection", "yolov11x"): YOLOv11KeypointsDetection,
    ("keypoint-detection", "yolov11n-pose"): YOLOv11KeypointsDetection,
    ("keypoint-detection", "yolov11s-pose"): YOLOv11KeypointsDetection,
    ("keypoint-detection", "yolov11m-pose"): YOLOv11KeypointsDetection,
    ("keypoint-detection", "yolov11l-pose"): YOLOv11KeypointsDetection,
    ("keypoint-detection", "yolov11x-pose"): YOLOv11KeypointsDetection,
    ("instance-segmentation", "stub"): InstanceSegmentationModelStub,
    (
        "instance-segmentation",
        "yolov5-seg",
    ): YOLOv5InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov5n-seg",
    ): YOLOv5InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov5s-seg",
    ): YOLOv5InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov5m-seg",
    ): YOLOv5InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov5l-seg",
    ): YOLOv5InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov5x-seg",
    ): YOLOv5InstanceSegmentation,
    (
        "instance-segmentation",
        "yolact",
    ): YOLACT,
    (
        "instance-segmentation",
        "yolov7-seg",
    ): YOLOv7InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov8n",
    ): YOLOv8InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov8",
    ): YOLOv8InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov8s",
    ): YOLOv8InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov8m",
    ): YOLOv8InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov8l",
    ): YOLOv8InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov8x",
    ): YOLOv8InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov8n-seg",
    ): YOLOv8InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov8s-seg",
    ): YOLOv8InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov8m-seg",
    ): YOLOv8InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov8l-seg",
    ): YOLOv8InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov8x-seg",
    ): YOLOv8InstanceSegmentation,
    (
        "instance-segmentation",
        "yolov8-seg",
    ): YOLOv8InstanceSegmentation,
    ("keypoint-detection", "stub"): KeypointsDetectionModelStub,
    ("keypoint-detection", "yolov8"): YOLOv8KeypointsDetection,
    ("keypoint-detection", "yolov8n"): YOLOv8KeypointsDetection,
    ("keypoint-detection", "yolov8s"): YOLOv8KeypointsDetection,
    ("keypoint-detection", "yolov8m"): YOLOv8KeypointsDetection,
    ("keypoint-detection", "yolov8l"): YOLOv8KeypointsDetection,
    ("keypoint-detection", "yolov8x"): YOLOv8KeypointsDetection,
    ("keypoint-detection", "yolov8n-pose"): YOLOv8KeypointsDetection,
    ("keypoint-detection", "yolov8s-pose"): YOLOv8KeypointsDetection,
    ("keypoint-detection", "yolov8m-pose"): YOLOv8KeypointsDetection,
    ("keypoint-detection", "yolov8l-pose"): YOLOv8KeypointsDetection,
    ("keypoint-detection", "yolov8x-pose"): YOLOv8KeypointsDetection,
}

try:
    if PALIGEMMA_ENABLED:
        from inference.models import LoRAPaliGemma, PaliGemma

        paligemma_models = {
            (
                "object-detection",
                "paligemma-3b-pt-224",
            ): PaliGemma,  # TODO: change when we have a new project type
            ("object-detection", "paligemma-3b-pt-448"): PaliGemma,
            ("object-detection", "paligemma-3b-pt-896"): PaliGemma,
            (
                "instance-segmentation",
                "paligemma-3b-pt-224",
            ): PaliGemma,  # TODO: change when we have a new project type
            ("instance-segmentation", "paligemma-3b-pt-448"): PaliGemma,
            ("instance-segmentation", "paligemma-3b-pt-896"): PaliGemma,
            (
                "object-detection",
                "paligemma-3b-pt-224-peft",
            ): LoRAPaliGemma,  # TODO: change when we have a new project type
            ("object-detection", "paligemma-3b-pt-448-peft"): LoRAPaliGemma,
            ("object-detection", "paligemma-3b-pt-896-peft"): LoRAPaliGemma,
            (
                "instance-segmentation",
                "paligemma-3b-pt-224-peft",
            ): LoRAPaliGemma,  # TODO: change when we have a new project type
            ("instance-segmentation", "paligemma-3b-pt-448-peft"): LoRAPaliGemma,
            ("instance-segmentation", "paligemma-3b-pt-896-peft"): LoRAPaliGemma,
            ("text-image-pairs", "paligemma2-3b-pt-224"): PaliGemma,
            ("text-image-pairs", "paligemma2-3b-pt-448"): PaliGemma,
            ("text-image-pairs", "paligemma2-3b-pt-896"): PaliGemma,
            ("text-image-pairs", "paligemma2-3b-pt-224-peft"): LoRAPaliGemma,
            ("text-image-pairs", "paligemma2-3b-pt-448-peft"): LoRAPaliGemma,
            ("text-image-pairs", "paligemma2-3b-pt-896-peft"): LoRAPaliGemma,
        }
        ROBOFLOW_MODEL_TYPES.update(paligemma_models)
except:
    warnings.warn(
        "Your `inference` configuration does not support PaliGemma model. "
        "Use pip install 'inference[transformers]' to install missing requirements."
        "To suppress this warning, set PALIGEMMA_ENABLED to False.",
        category=ModelDependencyMissing,
    )

try:
    if FLORENCE2_ENABLED:
        from inference.models import Florence2, LoRAFlorence2

        florence2_models = {
            (
                "object-detection",
                "florence-2-base",
            ): Florence2,  # TODO: change when we have a new project type
            ("object-detection", "florence-2-large"): Florence2,
            (
                "instance-segmentation",
                "florence-2-base",
            ): Florence2,  # TODO: change when we have a new project type
            ("instance-segmentation", "florence-2-large"): Florence2,
            (
                "object-detection",
                "florence-2-base-peft",
            ): LoRAFlorence2,  # TODO: change when we have a new project type
            (
                "text-image-pairs",
                "florence-2-base",
            ): Florence2,  # TODO: change when we have a new project type
            ("text-image-pairs", "florence-2-large"): Florence2,
            ("object-detection", "florence-2-large-peft"): LoRAFlorence2,
            (
                "instance-segmentation",
                "florence-2-base-peft",
            ): LoRAFlorence2,  # TODO: change when we have a new project type
            ("instance-segmentation", "florence-2-large-peft"): LoRAFlorence2,
            (
                "text-image-pairs",
                "florence-2-base-peft",
            ): LoRAFlorence2,
            ("text-image-pairs", "florence-2-large-peft"): LoRAFlorence2,
        }
        ROBOFLOW_MODEL_TYPES.update(florence2_models)
except:
    warnings.warn(
        "Your `inference` configuration does not support Florence2 model. "
        "Use pip install 'inference[transformers]' to install missing requirements."
        "To suppress this warning, set FLORENCE2_ENABLED to False.",
        category=ModelDependencyMissing,
    )

try:
    if QWEN_2_5_ENABLED:
        from inference.models import LoRAQwen25VL, Qwen25VL

        qwen25vl_models = {
            ("text-image-pairs", "qwen25-vl-7b"): Qwen25VL,
            ("text-image-pairs", "qwen25-vl-7b-peft"): LoRAQwen25VL,
        }
        ROBOFLOW_MODEL_TYPES.update(qwen25vl_models)
except:
    warnings.warn(
        "Your `inference` configuration does not support Qwen2.5-VL model. "
        "Use pip install 'inference[transformers]' to install missing requirements."
        "To suppress this warning, set QWEN_2_5_ENABLED to False.",
        category=ModelDependencyMissing,
    )


try:
    if CORE_MODEL_SAM_ENABLED:
        from inference.models import SegmentAnything

        ROBOFLOW_MODEL_TYPES[("embed", "sam")] = SegmentAnything
except:
    warnings.warn(
        "Your `inference` configuration does not support SAM model. "
        "Use pip install 'inference[sam]' to install missing requirements."
        "To suppress this warning, set CORE_MODEL_SAM_ENABLED to False.",
        category=ModelDependencyMissing,
    )
try:
    if CORE_MODEL_SAM2_ENABLED:
        from inference.models import SegmentAnything2

        ROBOFLOW_MODEL_TYPES[("embed", "sam2")] = SegmentAnything2
except:
    warnings.warn(
        "Your `inference` configuration does not support SAM2 model. "
        "Use pip install 'inference[sam]' to install missing requirements."
        "To suppress this warning, set CORE_MODEL_SAM2_ENABLED to False.",
        category=ModelDependencyMissing,
    )

try:
    if CORE_MODEL_CLIP_ENABLED:
        from inference.models import Clip

        ROBOFLOW_MODEL_TYPES[("embed", "clip")] = Clip
except:
    warnings.warn(
        "Your `inference` configuration does not support CLIP model. "
        "Use pip install 'inference[clip]' to install missing requirements."
        "To suppress this warning, set CORE_MODEL_CLIP_ENABLED to False.",
        category=ModelDependencyMissing,
    )

try:
    if CORE_MODEL_OWLV2_ENABLED:
        from inference.models.owlv2.owlv2 import OwlV2, SerializedOwlV2

        ROBOFLOW_MODEL_TYPES[("object-detection", "owlv2")] = OwlV2
        ROBOFLOW_MODEL_TYPES[("object-detection", "owlv2-finetuned")] = SerializedOwlV2
except:
    warnings.warn(
        "Your `inference` configuration does not support OWLv2 model. "
        "Use pip install 'inference[transformers]' to install missing requirements."
        "To suppress this warning, set CORE_MODEL_OWLV2_ENABLED to False.",
        category=ModelDependencyMissing,
    )

try:
    if CORE_MODEL_GAZE_ENABLED:
        from inference.models import Gaze

        ROBOFLOW_MODEL_TYPES[("gaze", "l2cs")] = Gaze
except:
    warnings.warn(
        "Your `inference` configuration does not support Gaze Detection model. "
        "Use pip install 'inference[gaze]' to install missing requirements."
        "To suppress this warning, set CORE_MODEL_GAZE_ENABLED to False.",
        category=ModelDependencyMissing,
    )

try:
    if SMOLVLM2_ENABLED:
        from inference.models.smolvlm.smolvlm import LoRASmolVLM, SmolVLM

        ROBOFLOW_MODEL_TYPES[("lmm", "smolvlm-2.2b-instruct")] = SmolVLM
        ROBOFLOW_MODEL_TYPES[("text-image-pairs", "smolvlm2-peft")] = LoRASmolVLM
        ROBOFLOW_MODEL_TYPES[("text-image-pairs", "smolvlm-256m-peft")] = LoRASmolVLM

except:
    warnings.warn(
        "Your `inference` configuration does not support SmolVLM2."
        "Use pip install 'inference[transformers]' to install missing requirements."
        "To suppress this warning, set SMOLVLM2_ENABLED to False.",
        category=ModelDependencyMissing,
    )


try:
    if DEPTH_ESTIMATION_ENABLED:
        from inference.models.depth_estimation.depthestimation import DepthEstimator

        ROBOFLOW_MODEL_TYPES[("depth-estimation", "small")] = DepthEstimator
except:
    warnings.warn(
        "Your `inference` configuration does not support Depth Estimation."
        "Use pip install 'inference[transformers]' to install missing requirements."
        "To suppress this warning, set DEPTH_ESTIMATION_ENABLED to False.",
        category=ModelDependencyMissing,
    )


try:
    if MOONDREAM2_ENABLED:
        from inference.models.moondream2.moondream2 import Moondream2

        ROBOFLOW_MODEL_TYPES[("lmm", "moondream2")] = Moondream2
except:
    warnings.warn(
        "Your `inference` configuration does not support Moondream2."
        "Use pip install 'inference[transformers]' to install missing requirements."
        "To suppress this warning, set MOONDREAM2_ENABLED to False.",
        category=ModelDependencyMissing,
    )

try:
    if CORE_MODEL_DOCTR_ENABLED:
        from inference.models import DocTR

        ROBOFLOW_MODEL_TYPES[("ocr", "doctr")] = DocTR
except:
    pass

try:
    if CORE_MODEL_TROCR_ENABLED:
        from inference.models import TrOCR

        ROBOFLOW_MODEL_TYPES[("ocr", "trocr")] = TrOCR
except:
    warnings.warn(
        "Your `inference` configuration does not support TrOCR model. "
        "Use pip install 'inference[transformers]' to install missing requirements."
        "To suppress this warning, set CORE_MODEL_TROCR_ENABLED to False.",
        category=ModelDependencyMissing,
    )

try:
    if CORE_MODEL_GROUNDINGDINO_ENABLED:
        from inference.models import GroundingDINO

        ROBOFLOW_MODEL_TYPES[("object-detection", "grounding-dino")] = GroundingDINO
except:
    warnings.warn(
        "Your `inference` configuration does not support GroundingDINO model. "
        "Use pip install 'inference[grounding-dino]' to install missing requirements."
        "To suppress this warning, set CORE_MODEL_GROUNDINGDINO_ENABLED to False.",
        category=ModelDependencyMissing,
    )

try:
    if CORE_MODEL_YOLO_WORLD_ENABLED:
        from inference.models import YOLOWorld

        ROBOFLOW_MODEL_TYPES[("object-detection", "yolo-world")] = YOLOWorld
except:
    warnings.warn(
        "Your `inference` configuration does not support YoloWorld model. "
        "Use pip install 'inference[yolo-world]' to install missing requirements."
        "To suppress this warning, set CORE_MODEL_YOLO_WORLD_ENABLED to False.",
        category=ModelDependencyMissing,
    )


try:
    if CORE_MODEL_PE_ENABLED:
        from inference.models import PerceptionEncoder

        ROBOFLOW_MODEL_TYPES[("embed", "perception_encoder")] = PerceptionEncoder
except:
    warnings.warn(
        "Your `inference` configuration does not support Perception Encoder."
        "Use pip install 'inference[transformers]' to install missing requirements."
        "To suppress this warning, set CORE_MODEL_PE_ENABLED to False.",
        category=ModelDependencyMissing,
    )


def get_model(model_id, api_key=API_KEY, **kwargs) -> Model:
    task, model = get_model_type(model_id, api_key=api_key)
    return ROBOFLOW_MODEL_TYPES[(task, model)](model_id, api_key=api_key, **kwargs)


def get_roboflow_model(*args, **kwargs):
    return get_model(*args, **kwargs)
