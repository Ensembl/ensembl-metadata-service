#  See the NOTICE file distributed with this work for additional information
#  regarding copyright ownership.
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#      http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import itertools
from ensembl.production.metadata.grpc import ensembl_metadata_pb2

from ensembl.production.metadata.grpc.config import MetadataConfig as cfg

from ensembl.production.metadata.api.genome import GenomeAdaptor
from ensembl.production.metadata.api.release import ReleaseAdaptor

from ensembl.production.metadata.grpc.protobuf_msg_factory import create_genome, create_karyotype, \
    create_top_level_statistics, create_top_level_statistics_by_uuid, create_assembly, create_species, \
    create_sub_species, create_genome_uuid, create_datasets, create_genome_sequence, create_release, \
    create_dataset_infos, populate_dataset_info


def connect_to_db():
    conn = GenomeAdaptor(
        metadata_uri=cfg.metadata_uri,
        taxonomy_uri=cfg.taxon_uri
    )
    return conn


def get_karyotype_information(db_conn, genome_uuid):
    if genome_uuid is None:
        return create_karyotype()

    karyotype_info_result = db_conn.fetch_sequences(
        genome_uuid=genome_uuid
    )

    if len(karyotype_info_result) == 1:
        return create_karyotype(karyotype_info_result[0])

    return create_karyotype()


def get_top_level_statistics(db_conn, organism_uuid):
    if organism_uuid is None:
        return create_top_level_statistics()

    stats_results = db_conn.fetch_genome_datasets(
        organism_uuid=organism_uuid,
        dataset_name="all"
    )

    statistics = []
    if len(stats_results) > 0:
        for result in stats_results:
            statistics.append({
                    'name': result.Attribute.name,
                    'label': result.Attribute.label,
                    'statistic_type': result.Attribute.type,
                    'statistic_value': result.DatasetAttribute.value
                })
        return create_top_level_statistics({
            'organism_uuid': organism_uuid,
            'statistics': statistics
        })

    return create_top_level_statistics()


def get_top_level_statistics_by_uuid(db_conn, genome_uuid):
    if genome_uuid is None:
        return create_top_level_statistics_by_uuid()

    stats_results = db_conn.fetch_genome_datasets(
        genome_uuid=genome_uuid,
        dataset_name="all"
    )

    statistics = []
    if len(stats_results) > 0:
        for result in stats_results:
            statistics.append({
                'name': result.Attribute.name,
                'label': result.Attribute.label,
                'statistic_type': result.Attribute.type,
                'statistic_value': result.DatasetAttribute.value
            })
        return create_top_level_statistics_by_uuid(
            ({"genome_uuid": genome_uuid, "statistics": statistics})
        )

    return create_top_level_statistics_by_uuid()


def get_assembly_information(db_conn, assembly_uuid):
    if assembly_uuid is None:
        return create_assembly()

    assembly_results = db_conn.fetch_sequences(
        assembly_uuid=assembly_uuid
    )
    if len(assembly_results) > 0:
        return create_assembly(assembly_results[0])

    return create_assembly()


def get_genomes_from_assembly_accession_iterator(db_conn, assembly_accession):
    if assembly_accession is None:
        return create_genome()

    genome_results = db_conn.fetch_genomes(
        assembly_accession=assembly_accession
    )
    for genome in genome_results:
        yield create_genome(genome)


def get_species_information(db_conn, genome_uuid):
    if genome_uuid is None:
        return create_species()

    species_results = db_conn.fetch_genomes(
        genome_uuid=genome_uuid
    )
    if len(species_results) == 1:
        tax_id = species_results[0].Organism.taxonomy_id
        taxo_results = db_conn.fetch_taxonomy_names(tax_id)
        return create_species(species_results[0], taxo_results[tax_id])

    return create_species()


def get_sub_species_info(db_conn, organism_uuid):
    if organism_uuid is None:
        return create_sub_species()

    sub_species_results = db_conn.fetch_genomes(
        organism_uuid=organism_uuid
    )

    species_name = []
    species_type = []
    if len(sub_species_results) > 0:
        for result in sub_species_results:
            if result.OrganismGroup.type not in species_type:
                species_type.append(result.OrganismGroup.type)
            if result.OrganismGroup.name not in species_name:
                species_name.append(result.OrganismGroup.name)

        return create_sub_species({
            'organism_uuid': organism_uuid,
            'species_type': species_type,
            'species_name': species_name
        })

    return create_sub_species()


def get_genome_uuid(db_conn, ensembl_name, assembly_name):
    if ensembl_name is None or assembly_name is None:
        return create_genome_uuid()

    genome_uuid_result = db_conn.fetch_genomes(
        ensembl_name=ensembl_name,
        assembly_name=assembly_name
    )

    if len(genome_uuid_result) == 1:
        return create_genome_uuid(
            {"genome_uuid": genome_uuid_result[0].Genome.genome_uuid}
        )

    return create_genome_uuid()


def get_genome_by_uuid(db_conn, genome_uuid, release_version):
    if genome_uuid is None:
        return create_genome()

    genome_results = db_conn.fetch_genomes(
        genome_uuid=genome_uuid,
        release_version=release_version
    )

    if len(genome_results) == 1:
        return create_genome(genome_results[0])
    return create_genome()


def get_genomes_by_keyword_iterator(db_conn, keyword, release_version):
    if not keyword:
        return create_genome()

    genome_results = db_conn.fetch_genome_by_keyword(
        keyword=keyword,
        release_version=release_version
    )

    if len(genome_results) > 0:
        # Create an empty list to store the most recent genomes
        most_recent_genomes = []
        # Group `genome_results` based on the `assembly_accession` field
        for _, genome_release_group in itertools.groupby(genome_results, lambda r: r.Assembly.accession):
            # Sort the genomes in each group based on the `release_version` field in descending order
            sorted_genomes = sorted(genome_release_group, key=lambda g: g.EnsemblRelease.version, reverse=True)
            # Select the most recent genome from the sorted group (first element)
            most_recent_genome = sorted_genomes[0]
            # Add the most recent genome to the `most_recent_genomes` list
            most_recent_genomes.append(most_recent_genome)

        for genome_row in most_recent_genomes:
            yield create_genome(genome_row)

        return create_genome()


def get_genome_by_name(db_conn, ensembl_name, site_name, release_version):
    if ensembl_name is None and site_name is None:
        return create_genome()

    genome_results = db_conn.fetch_genomes(
        ensembl_name=ensembl_name,
        site_name=site_name,
        release_version=release_version
    )
    if len(genome_results) == 1:
        return create_genome(genome_results[0])
    return create_genome()


def get_datasets_list_by_uuid(db_conn, genome_uuid, release_version=0):
    if genome_uuid is None:
        return create_datasets()

    datasets_results = db_conn.fetch_genome_datasets(
        genome_uuid=genome_uuid,
        # fetch all datasets, default is 'assembly' only
        dataset_name="all",
        release_version=release_version
    )

    if len(datasets_results) > 0:
        # ds_obj_dict where all datasets are stored as:
        # { dataset_type_1: [datasets_dt1_1, datasets_dt1_2], dataset_type_2: [datasets_dt2_1] }
        ds_obj_dict = {}
        for result in datasets_results:
            dataset_type = result.DatasetType.name
            # Populate the objects bottom up
            datasets_info = populate_dataset_info(result)
            # Construct the datasets dictionary
            if dataset_type in ds_obj_dict:
                ds_obj_dict[dataset_type].append(datasets_info)
            else:
                ds_obj_dict[dataset_type] = [datasets_info]

        dataset_object_dict = {}
        # map each datasets list (e.g: [datasets_dt1_1, datasets_dt1_2]) to DatasetInfos
        for dataset_type_key in ds_obj_dict:
            dataset_object_dict[dataset_type_key] = ensembl_metadata_pb2.DatasetInfos(
                dataset_infos=ds_obj_dict[dataset_type_key]
            )

        return create_datasets({
            'genome_uuid': genome_uuid,
            'datasets': dataset_object_dict
        })

    return create_datasets()


def genome_sequence_iterator(db_conn, genome_uuid, chromosomal_only):
    if genome_uuid is None:
        return

    assembly_sequence_results = db_conn.fetch_sequences(
        genome_uuid=genome_uuid,
        chromosomal_only=chromosomal_only,
    )
    for result in assembly_sequence_results:
        yield create_genome_sequence(result)


def release_iterator(metadata_db, site_name, release_version, current_only):
    conn = ReleaseAdaptor(metadata_uri=cfg.metadata_uri)

    # set release_version/site_name to None if it's an empty list
    release_version = release_version or None
    site_name = site_name or None

    release_results = conn.fetch_releases(
        release_version=release_version,
        current_only=current_only,
        site_name=site_name
    )

    for result in release_results:
        yield create_release(result)


def release_by_uuid_iterator(metadata_db, genome_uuid):
    if genome_uuid is None:
        return

    conn = ReleaseAdaptor(metadata_uri=cfg.metadata_uri)
    release_results = conn.fetch_releases_for_genome(
        genome_uuid=genome_uuid,
    )

    for result in release_results:
        yield create_release(result)


def get_dataset_by_genome_and_dataset_type(db_conn, genome_uuid, requested_dataset_type):
    if genome_uuid is None:
        return create_dataset_infos()

    dataset_results = db_conn.fetch_genome_datasets(
        genome_uuid=genome_uuid,
        dataset_type=requested_dataset_type
    )
    return create_dataset_infos(genome_uuid, requested_dataset_type, dataset_results)