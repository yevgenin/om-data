from dataclasses import dataclass

import numpy


@dataclass(frozen=True)
class SeqLabeledExported:
    name: str
    patterns: tuple[str, ...]


@dataclass(frozen=True)
class OrganismExported:
    name: str
    description: str


@dataclass(frozen=True)
class DatasetMetadataExported:
    timestamp: str
    organism: OrganismExported
    seq_labeled: SeqLabeledExported
    scan_set_metadata: dict


@dataclass(frozen=True)
class ImageMetadataExported:
    file: str
    processed_image_uuid: int
    timestamps_sec: list[float]
    stage_x_um: float
    stage_y_um: float
    image_read_metadata: dict


@dataclass(frozen=True)
class ImageSegmentExported:
    image_segment_uuid: int
    profile_image_seq: ndarray
    profile_coords_map: ndarray
    profile_curve_coords: ndarray


@dataclass(frozen=True)
class SegmentedImageExported:
    image_metadata: ImageMetadataExported
    image_segments: list[ImageSegmentExported]


@dataclass(frozen=True)
class ProcessedImageExported:
    processed_image_uuid: int

    captured_image_seq: ndarray
    captured_image_seq_intensity_corrected: ndarray
    intensity_correction_map: ndarray

    segmented_image: SegmentedImageExported


@dataclass(frozen=True)
class GenomeSeqLabeledExported:
    genome_seq_uuid: int

    organism: OrganismExported
    genome_seq_labeled: SeqLabeledExported
    genome_seq_bytes: bytes
    genome_seq_bytes_hash: int
    genome_seq_metadata: dict
    is_circular: bool
    labeled_mask: ndarray
    labeled_mask_hash: int = None


@dataclass(frozen=True)
class GenomesExported:
    genome_seqs: dict[OrganismExported, GenomeSeqLabeledExported]
