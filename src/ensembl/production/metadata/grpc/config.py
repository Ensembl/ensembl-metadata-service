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
import os


class MetadataConfig:
    metadata_uri = os.environ.get("METADATA_URI", f"mysql+pymysql://ensembl@localhost:3306/ensembl_genome_metadata")
    taxon_uri = os.environ.get("TAXONOMY_URI", f"mysql+pymysql://ensembl@localhost:3306/ncbi_taxonomy")
    pool_size = os.environ.get("POOL_SIZE", 20)
    max_overflow = os.environ.get("MAX_OVERFLOW", 0)
    pool_recycle = os.environ.get("POOL_RECYCLE", 50)
    allow_unreleased = os.environ.get("ALLOW_UNRELEASED", False)
