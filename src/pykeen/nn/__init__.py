# -*- coding: utf-8 -*-

"""PyKEEN internal "nn" module."""

from class_resolver import ClassResolver

from . import init
from .combination import (
    Combination,
    ComplexSeparatedCombination,
    ConcatAggregationCombination,
    ConcatCombination,
    ConcatProjectionCombination,
    GatedCombination,
)
from .message_passing import RGCNRepresentation
from .modules import (
    AutoSFInteraction,
    BoxEInteraction,
    ComplExInteraction,
    ConvEInteraction,
    ConvKBInteraction,
    CPInteraction,
    CrossEInteraction,
    DistMAInteraction,
    DistMultInteraction,
    ERMLPEInteraction,
    ERMLPInteraction,
    HolEInteraction,
    Interaction,
    KG2EInteraction,
    LineaREInteraction,
    MonotonicAffineTransformationInteraction,
    MultiLinearTuckerInteraction,
    MuREInteraction,
    NTNInteraction,
    PairREInteraction,
    ProjEInteraction,
    QuatEInteraction,
    RESCALInteraction,
    RotatEInteraction,
    SEInteraction,
    SimplEInteraction,
    TorusEInteraction,
    TransDInteraction,
    TransEInteraction,
    TransFInteraction,
    TransformerInteraction,
    TransHInteraction,
    TransRInteraction,
    TripleREInteraction,
    TuckerInteraction,
    UMInteraction,
    interaction_resolver,
)
from .node_piece import NodePieceRepresentation, TokenizationRepresentation, tokenizer_resolver
from .pyg import (
    FeaturizedMessagePassingRepresentation,
    SimpleMessagePassingRepresentation,
    TypedMessagePassingRepresentation,
)
from .representation import (
    CombinedRepresentation,
    Embedding,
    LowRankRepresentation,
    Representation,
    SubsetRepresentation,
    TextRepresentation,
    WikidataTextRepresentation,
)

__all__ = [
    # REPRESENTATION
    # base
    "Representation",
    # concrete
    "Embedding",
    "FeaturizedMessagePassingRepresentation",
    "LowRankRepresentation",
    "NodePieceRepresentation",
    "RGCNRepresentation",
    "SimpleMessagePassingRepresentation",
    "SubsetRepresentation",
    "TokenizationRepresentation",
    "TypedMessagePassingRepresentation",
    "FeaturizedMessagePassingRepresentation",
    "CombinedRepresentation",
    "TextRepresentation",
    "WikidataTextRepresentation",
    "tokenizer_resolver",
    "representation_resolver",
    # INITIALIZER
    "init",
    # INTERACTIONS
    "Interaction",
    # Adapter classes
    "MonotonicAffineTransformationInteraction",
    # Concrete Classes
    "AutoSFInteraction",
    "BoxEInteraction",
    "ComplExInteraction",
    "ConvEInteraction",
    "ConvKBInteraction",
    "CPInteraction",
    "CrossEInteraction",
    "DistMAInteraction",
    "DistMultInteraction",
    "ERMLPEInteraction",
    "ERMLPInteraction",
    "HolEInteraction",
    "KG2EInteraction",
    "LineaREInteraction",
    "MultiLinearTuckerInteraction",
    "MuREInteraction",
    "NTNInteraction",
    "PairREInteraction",
    "ProjEInteraction",
    "QuatEInteraction",
    "RESCALInteraction",
    "RotatEInteraction",
    "SEInteraction",
    "SimplEInteraction",
    "TorusEInteraction",
    "TransDInteraction",
    "TransEInteraction",
    "TransFInteraction",
    "TransformerInteraction",
    "TransHInteraction",
    "TransRInteraction",
    "TripleREInteraction",
    "TuckerInteraction",
    "UMInteraction",
    "interaction_resolver",
    # combinations
    "Combination",
    "ComplexSeparatedCombination",
    "ConcatAggregationCombination",
    "ConcatCombination",
    "ConcatProjectionCombination",
    "GatedCombination",
]

representation_resolver: ClassResolver[Representation] = ClassResolver.from_subclasses(
    base=Representation,
    default=Embedding,
)
