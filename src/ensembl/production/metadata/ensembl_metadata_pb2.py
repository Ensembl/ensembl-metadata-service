# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ensembl_metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ensembl_metadata.proto',
  package='ensembl_metadata',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16\x65nsembl_metadata.proto\x12\x10\x65nsembl_metadata\"\xc5\x01\n\x06Genome\x12\x13\n\x0bgenome_uuid\x18\x01 \x01(\t\x12\x14\n\x0c\x65nsembl_name\x18\x02 \x01(\t\x12\x10\n\x08url_name\x18\x03 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x04 \x01(\t\x12\x12\n\nis_current\x18\x05 \x01(\x08\x12,\n\x08\x61ssembly\x18\x06 \x01(\x0b\x32\x1a.ensembl_metadata.Assembly\x12&\n\x05taxon\x18\x07 \x01(\x0b\x32\x17.ensembl_metadata.Taxon\"\x93\x01\n\x07Species\x12\x13\n\x0bgenome_uuid\x18\x01 \x01(\t\x12\x13\n\x0b\x63ommon_name\x18\x02 \x01(\t\x12\x18\n\x10ncbi_common_name\x18\x04 \x01(\t\x12\x10\n\x08taxon_id\x18\x05 \x01(\r\x12\x17\n\x0fscientific_name\x18\x06 \x01(\t\x12\x19\n\x11\x61lternative_names\x18\x07 \x03(\t\"M\n\x08\x41ssembly\x12\x11\n\taccession\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tucsc_name\x18\x03 \x01(\t\x12\r\n\x05level\x18\x04 \x01(\t\"Z\n\x05Taxon\x12\x13\n\x0btaxonomy_id\x18\x01 \x01(\r\x12\x17\n\x0fscientific_name\x18\x02 \x01(\t\x12\x0e\n\x06strain\x18\x03 \x01(\t\x12\x13\n\x0b\x63ommon_name\x18\x04 \x03(\t\"\x9c\x01\n\x07Release\x12\x17\n\x0frelease_version\x18\x01 \x01(\r\x12\x14\n\x0crelease_date\x18\x02 \x01(\t\x12\x15\n\rrelease_label\x18\x03 \x01(\t\x12\x12\n\nis_current\x18\x04 \x01(\x08\x12\x11\n\tsite_name\x18\x05 \x01(\t\x12\x12\n\nsite_label\x18\x06 \x01(\t\x12\x10\n\x08site_uri\x18\x07 \x01(\t\"q\n\x0eGenomeSequence\x12\x11\n\taccession\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11sequence_location\x18\x03 \x01(\t\x12\x0e\n\x06length\x18\x04 \x01(\r\x12\x13\n\x0b\x63hromosomal\x18\x05 \x01(\x08\"(\n\x11GenomeUUIDRequest\x12\x13\n\x0bgenome_uuid\x18\x01 \x01(\t\"U\n\x11GenomeNameRequest\x12\x14\n\x0c\x65nsembl_name\x18\x01 \x01(\t\x12\x11\n\tsite_name\x18\x02 \x01(\t\x12\x17\n\x0frelease_version\x18\x03 \x01(\r\"R\n\x0eReleaseRequest\x12\x11\n\tsite_name\x18\x01 \x03(\t\x12\x17\n\x0frelease_version\x18\x02 \x03(\r\x12\x14\n\x0c\x63urrent_only\x18\x03 \x01(\x08\"F\n\x15GenomeSequenceRequest\x12\x13\n\x0bgenome_uuid\x18\x01 \x01(\t\x12\x18\n\x10\x63hromosomal_only\x18\x02 \x01(\x08\x32\x9f\x04\n\x0f\x45nsemblMetadata\x12R\n\x0fGetGenomeByUUID\x12#.ensembl_metadata.GenomeUUIDRequest\x1a\x18.ensembl_metadata.Genome\"\x00\x12Y\n\x15GetSpeciesInformation\x12#.ensembl_metadata.GenomeUUIDRequest\x1a\x19.ensembl_metadata.Species\"\x00\x12R\n\x0fGetGenomeByName\x12#.ensembl_metadata.GenomeNameRequest\x1a\x18.ensembl_metadata.Genome\"\x00\x12M\n\nGetRelease\x12 .ensembl_metadata.ReleaseRequest\x1a\x19.ensembl_metadata.Release\"\x00\x30\x01\x12V\n\x10GetReleaseByUUID\x12#.ensembl_metadata.GenomeUUIDRequest\x1a\x19.ensembl_metadata.Release\"\x00\x30\x01\x12\x62\n\x11GetGenomeSequence\x12\'.ensembl_metadata.GenomeSequenceRequest\x1a .ensembl_metadata.GenomeSequence\"\x00\x30\x01\x62\x06proto3'
)




_GENOME = _descriptor.Descriptor(
  name='Genome',
  full_name='ensembl_metadata.Genome',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='genome_uuid', full_name='ensembl_metadata.Genome.genome_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ensembl_name', full_name='ensembl_metadata.Genome.ensembl_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url_name', full_name='ensembl_metadata.Genome.url_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='ensembl_metadata.Genome.display_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_current', full_name='ensembl_metadata.Genome.is_current', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='assembly', full_name='ensembl_metadata.Genome.assembly', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='taxon', full_name='ensembl_metadata.Genome.taxon', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=242,
)


_SPECIES = _descriptor.Descriptor(
  name='Species',
  full_name='ensembl_metadata.Species',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='genome_uuid', full_name='ensembl_metadata.Species.genome_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='common_name', full_name='ensembl_metadata.Species.common_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ncbi_common_name', full_name='ensembl_metadata.Species.ncbi_common_name', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='taxon_id', full_name='ensembl_metadata.Species.taxon_id', index=3,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scientific_name', full_name='ensembl_metadata.Species.scientific_name', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alternative_names', full_name='ensembl_metadata.Species.alternative_names', index=5,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=245,
  serialized_end=392,
)


_ASSEMBLY = _descriptor.Descriptor(
  name='Assembly',
  full_name='ensembl_metadata.Assembly',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accession', full_name='ensembl_metadata.Assembly.accession', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='ensembl_metadata.Assembly.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ucsc_name', full_name='ensembl_metadata.Assembly.ucsc_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='ensembl_metadata.Assembly.level', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=394,
  serialized_end=471,
)


_TAXON = _descriptor.Descriptor(
  name='Taxon',
  full_name='ensembl_metadata.Taxon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='taxonomy_id', full_name='ensembl_metadata.Taxon.taxonomy_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scientific_name', full_name='ensembl_metadata.Taxon.scientific_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='strain', full_name='ensembl_metadata.Taxon.strain', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='common_name', full_name='ensembl_metadata.Taxon.common_name', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=473,
  serialized_end=563,
)


_RELEASE = _descriptor.Descriptor(
  name='Release',
  full_name='ensembl_metadata.Release',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='release_version', full_name='ensembl_metadata.Release.release_version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='release_date', full_name='ensembl_metadata.Release.release_date', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='release_label', full_name='ensembl_metadata.Release.release_label', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_current', full_name='ensembl_metadata.Release.is_current', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='site_name', full_name='ensembl_metadata.Release.site_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='site_label', full_name='ensembl_metadata.Release.site_label', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='site_uri', full_name='ensembl_metadata.Release.site_uri', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=566,
  serialized_end=722,
)


_GENOMESEQUENCE = _descriptor.Descriptor(
  name='GenomeSequence',
  full_name='ensembl_metadata.GenomeSequence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accession', full_name='ensembl_metadata.GenomeSequence.accession', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='ensembl_metadata.GenomeSequence.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_location', full_name='ensembl_metadata.GenomeSequence.sequence_location', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='ensembl_metadata.GenomeSequence.length', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chromosomal', full_name='ensembl_metadata.GenomeSequence.chromosomal', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=724,
  serialized_end=837,
)


_GENOMEUUIDREQUEST = _descriptor.Descriptor(
  name='GenomeUUIDRequest',
  full_name='ensembl_metadata.GenomeUUIDRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='genome_uuid', full_name='ensembl_metadata.GenomeUUIDRequest.genome_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=839,
  serialized_end=879,
)


_GENOMENAMEREQUEST = _descriptor.Descriptor(
  name='GenomeNameRequest',
  full_name='ensembl_metadata.GenomeNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ensembl_name', full_name='ensembl_metadata.GenomeNameRequest.ensembl_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='site_name', full_name='ensembl_metadata.GenomeNameRequest.site_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='release_version', full_name='ensembl_metadata.GenomeNameRequest.release_version', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=881,
  serialized_end=966,
)


_RELEASEREQUEST = _descriptor.Descriptor(
  name='ReleaseRequest',
  full_name='ensembl_metadata.ReleaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='site_name', full_name='ensembl_metadata.ReleaseRequest.site_name', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='release_version', full_name='ensembl_metadata.ReleaseRequest.release_version', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='current_only', full_name='ensembl_metadata.ReleaseRequest.current_only', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=968,
  serialized_end=1050,
)


_GENOMESEQUENCEREQUEST = _descriptor.Descriptor(
  name='GenomeSequenceRequest',
  full_name='ensembl_metadata.GenomeSequenceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='genome_uuid', full_name='ensembl_metadata.GenomeSequenceRequest.genome_uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chromosomal_only', full_name='ensembl_metadata.GenomeSequenceRequest.chromosomal_only', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1052,
  serialized_end=1122,
)

_GENOME.fields_by_name['assembly'].message_type = _ASSEMBLY
_GENOME.fields_by_name['taxon'].message_type = _TAXON
DESCRIPTOR.message_types_by_name['Genome'] = _GENOME
DESCRIPTOR.message_types_by_name['Species'] = _SPECIES
DESCRIPTOR.message_types_by_name['Assembly'] = _ASSEMBLY
DESCRIPTOR.message_types_by_name['Taxon'] = _TAXON
DESCRIPTOR.message_types_by_name['Release'] = _RELEASE
DESCRIPTOR.message_types_by_name['GenomeSequence'] = _GENOMESEQUENCE
DESCRIPTOR.message_types_by_name['GenomeUUIDRequest'] = _GENOMEUUIDREQUEST
DESCRIPTOR.message_types_by_name['GenomeNameRequest'] = _GENOMENAMEREQUEST
DESCRIPTOR.message_types_by_name['ReleaseRequest'] = _RELEASEREQUEST
DESCRIPTOR.message_types_by_name['GenomeSequenceRequest'] = _GENOMESEQUENCEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Genome = _reflection.GeneratedProtocolMessageType('Genome', (_message.Message,), {
  'DESCRIPTOR' : _GENOME,
  '__module__' : 'ensembl_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ensembl_metadata.Genome)
  })
_sym_db.RegisterMessage(Genome)

Species = _reflection.GeneratedProtocolMessageType('Species', (_message.Message,), {
  'DESCRIPTOR' : _SPECIES,
  '__module__' : 'ensembl_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ensembl_metadata.Species)
  })
_sym_db.RegisterMessage(Species)

Assembly = _reflection.GeneratedProtocolMessageType('Assembly', (_message.Message,), {
  'DESCRIPTOR' : _ASSEMBLY,
  '__module__' : 'ensembl_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ensembl_metadata.Assembly)
  })
_sym_db.RegisterMessage(Assembly)

Taxon = _reflection.GeneratedProtocolMessageType('Taxon', (_message.Message,), {
  'DESCRIPTOR' : _TAXON,
  '__module__' : 'ensembl_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ensembl_metadata.Taxon)
  })
_sym_db.RegisterMessage(Taxon)

Release = _reflection.GeneratedProtocolMessageType('Release', (_message.Message,), {
  'DESCRIPTOR' : _RELEASE,
  '__module__' : 'ensembl_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ensembl_metadata.Release)
  })
_sym_db.RegisterMessage(Release)

GenomeSequence = _reflection.GeneratedProtocolMessageType('GenomeSequence', (_message.Message,), {
  'DESCRIPTOR' : _GENOMESEQUENCE,
  '__module__' : 'ensembl_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ensembl_metadata.GenomeSequence)
  })
_sym_db.RegisterMessage(GenomeSequence)

GenomeUUIDRequest = _reflection.GeneratedProtocolMessageType('GenomeUUIDRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENOMEUUIDREQUEST,
  '__module__' : 'ensembl_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ensembl_metadata.GenomeUUIDRequest)
  })
_sym_db.RegisterMessage(GenomeUUIDRequest)

GenomeNameRequest = _reflection.GeneratedProtocolMessageType('GenomeNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENOMENAMEREQUEST,
  '__module__' : 'ensembl_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ensembl_metadata.GenomeNameRequest)
  })
_sym_db.RegisterMessage(GenomeNameRequest)

ReleaseRequest = _reflection.GeneratedProtocolMessageType('ReleaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _RELEASEREQUEST,
  '__module__' : 'ensembl_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ensembl_metadata.ReleaseRequest)
  })
_sym_db.RegisterMessage(ReleaseRequest)

GenomeSequenceRequest = _reflection.GeneratedProtocolMessageType('GenomeSequenceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENOMESEQUENCEREQUEST,
  '__module__' : 'ensembl_metadata_pb2'
  # @@protoc_insertion_point(class_scope:ensembl_metadata.GenomeSequenceRequest)
  })
_sym_db.RegisterMessage(GenomeSequenceRequest)



_ENSEMBLMETADATA = _descriptor.ServiceDescriptor(
  name='EnsemblMetadata',
  full_name='ensembl_metadata.EnsemblMetadata',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1125,
  serialized_end=1668,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetGenomeByUUID',
    full_name='ensembl_metadata.EnsemblMetadata.GetGenomeByUUID',
    index=0,
    containing_service=None,
    input_type=_GENOMEUUIDREQUEST,
    output_type=_GENOME,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSpeciesInformation',
    full_name='ensembl_metadata.EnsemblMetadata.GetSpeciesInformation',
    index=1,
    containing_service=None,
    input_type=_GENOMEUUIDREQUEST,
    output_type=_SPECIES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetGenomeByName',
    full_name='ensembl_metadata.EnsemblMetadata.GetGenomeByName',
    index=2,
    containing_service=None,
    input_type=_GENOMENAMEREQUEST,
    output_type=_GENOME,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetRelease',
    full_name='ensembl_metadata.EnsemblMetadata.GetRelease',
    index=3,
    containing_service=None,
    input_type=_RELEASEREQUEST,
    output_type=_RELEASE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetReleaseByUUID',
    full_name='ensembl_metadata.EnsemblMetadata.GetReleaseByUUID',
    index=4,
    containing_service=None,
    input_type=_GENOMEUUIDREQUEST,
    output_type=_RELEASE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetGenomeSequence',
    full_name='ensembl_metadata.EnsemblMetadata.GetGenomeSequence',
    index=5,
    containing_service=None,
    input_type=_GENOMESEQUENCEREQUEST,
    output_type=_GENOMESEQUENCE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENSEMBLMETADATA)

DESCRIPTOR.services_by_name['EnsemblMetadata'] = _ENSEMBLMETADATA

# @@protoc_insertion_point(module_scope)
