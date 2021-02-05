# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Il10(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il19_interleukin_19_plus_strand = models.TextField(db_column='Gene_IL19_interleukin_19_plus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_il10_interleukin_10_minus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL10_interleukin_10_minus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il10_interleukin_10_minus_strand = models.TextField(db_column='Gene_IL10_interleukin_10_minus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_il19_interleukin_19_plus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL19_interleukin_19_plus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il10_interleukin_10_minus_strand_500b_downstream_vari = models.TextField(db_column='Gene_IL10_interleukin_10_minus_strand__500B_Downstream_Vari', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il10'


class Il11(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il11_interleukin_11_minus_strand = models.TextField(db_column='Gene_IL11_interleukin_11_minus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_fam71e2_family_with_sequence_similarity_71_member_e2_min = models.TextField(db_column='Gene_FAM71E2_family_with_sequence_similarity_71_member_E2_min', blank=True, null=True)  # Field name made lowercase.
    gene_il11_interleukin_11_minus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL11_interleukin_11_minus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il11_interleukin_11_minus_strand_500b_downstream_vari = models.TextField(db_column='Gene_IL11_interleukin_11_minus_strand__500B_Downstream_Vari', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il11'


class Il12A(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il12a_interleukin_12a_plus_strand = models.TextField(db_column='Gene_IL12A_interleukin_12A_plus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_il12a_as1_il12a_antisense_rna_1_minus_strand = models.TextField(db_column='Gene_IL12A_AS1_IL12A_antisense_RNA_1_minus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il12a_interleukin_12a_plus_strand_500b_downstream_var = models.TextField(db_column='Gene_IL12A_interleukin_12A_plus_strand__500B_Downstream_Var', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il12a_interleukin_12a_plus_strand_2kb_upstream_varian = models.TextField(db_column='Gene_IL12A_interleukin_12A_plus_strand__2KB_Upstream_Varian', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il12a'


class Il12B(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il12b_interleukin_12b_minus_strand = models.TextField(db_column='Gene_IL12B_interleukin_12B_minus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_loc105377683_uncharacterized_loc105377683_plus_strand = models.TextField(db_column='Gene_LOC105377683_uncharacterized_LOC105377683_plus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_loc107986469_uncharacterized_loc107986469_plus_strand = models.TextField(db_column='Gene_LOC107986469_uncharacterized_LOC107986469_plus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_loc105377683_uncharacterized_loc105377683_plus_strand_field = models.TextField(db_column='Gene_LOC105377683_uncharacterized_LOC105377683_plus_strand_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    gene_loc107986469_uncharacterized_loc107986469_plus_strand_field = models.TextField(db_column='Gene_LOC107986469_uncharacterized_LOC107986469_plus_strand_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    gene_loc285626_uncharacterized_loc285626_plus_strand_2kb_u = models.TextField(db_column='Gene_LOC285626_uncharacterized_LOC285626_plus_strand__2KB_U', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_loc107986469_uncharacterized_loc107986469_plus_strand_1 = models.TextField(db_column='Gene_LOC107986469_uncharacterized_LOC107986469_plus_strand_1', blank=True, null=True)  # Field name made lowercase.
    gene_il12b_interleukin_12b_minus_strand_500b_downstream_va = models.TextField(db_column='Gene_IL12B_interleukin_12B_minus_strand__500B_Downstream_Va', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il12b_interleukin_12b_minus_strand_2kb_upstream_varia = models.TextField(db_column='Gene_IL12B_interleukin_12B_minus_strand__2KB_Upstream_Varia', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_loc285626_uncharacterized_loc285626_plus_strand = models.TextField(db_column='Gene_LOC285626_uncharacterized_LOC285626_plus_strand', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'il12b'


class Il13(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il13_interleukin_13_plus_strand = models.TextField(db_column='Gene_IL13_interleukin_13_plus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_th2lcrr_t_helper_type_2_locus_control_region_associated_r = models.TextField(db_column='Gene_TH2LCRR_T_helper_type_2_locus_control_region_associated_R', blank=True, null=True)  # Field name made lowercase.
    gene_il13_interleukin_13_plus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL13_interleukin_13_plus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_th2lcrr_t_helper_type_2_locus_control_region_associated_1 = models.TextField(db_column='Gene_TH2LCRR_T_helper_type_2_locus_control_region_associated_1', blank=True, null=True)  # Field name made lowercase.
    gene_il13_interleukin_13_plus_strand_500b_downstream_varia = models.TextField(db_column='Gene_IL13_interleukin_13_plus_strand__500B_Downstream_Varia', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il13'


class Il15(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il15_interleukin_15_plus_strand = models.TextField(db_column='Gene_IL15_interleukin_15_plus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il15_interleukin_15_plus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL15_interleukin_15_plus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il15_interleukin_15_plus_strand_500b_downstream_varia = models.TextField(db_column='Gene_IL15_interleukin_15_plus_strand__500B_Downstream_Varia', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il15'


class Il16(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il16_interleukin_16_plus_strand = models.TextField(db_column='Gene_IL16_interleukin_16_plus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_stard5_star_related_lipid_transfer_domain_containing_5_m = models.TextField(db_column='Gene_STARD5_StAR_related_lipid_transfer_domain_containing_5_m', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_stard5_star_related_lipid_transfer_domain_containing_5_1 = models.TextField(db_column='Gene_STARD5_StAR_related_lipid_transfer_domain_containing_5_1', blank=True, null=True)  # Field name made lowercase.
    gene_il16_interleukin_16_plus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL16_interleukin_16_plus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il16_interleukin_16_plus_strand_500b_downstream_varia = models.TextField(db_column='Gene_IL16_interleukin_16_plus_strand__500B_Downstream_Varia', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il16'


class Il17A(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il17a_interleukin_17a_plus_strand = models.TextField(db_column='Gene_IL17A_interleukin_17A_plus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il17a_interleukin_17a_plus_strand_2kb_upstream_varian = models.TextField(db_column='Gene_IL17A_interleukin_17A_plus_strand__2KB_Upstream_Varian', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il17a_interleukin_17a_plus_strand_500b_downstream_var = models.TextField(db_column='Gene_IL17A_interleukin_17A_plus_strand__500B_Downstream_Var', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il17a'


class Il17B(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_pcyox1l_prenylcysteine_oxidase_1_like_plus_strand = models.TextField(db_column='Gene_PCYOX1L_prenylcysteine_oxidase_1_like_plus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_il17b_interleukin_17b_minus_strand = models.TextField(db_column='Gene_IL17B_interleukin_17B_minus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_loc101927046_uncharacterized_loc101927046_plus_strand = models.TextField(db_column='Gene_LOC101927046_uncharacterized_LOC101927046_plus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_loc101927046_uncharacterized_loc101927046_plus_strand_field = models.TextField(db_column='Gene_LOC101927046_uncharacterized_LOC101927046_plus_strand_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    gene_il17b_interleukin_17b_minus_strand_500b_downstream_va = models.TextField(db_column='Gene_IL17B_interleukin_17B_minus_strand__500B_Downstream_Va', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il17b_interleukin_17b_minus_strand_2kb_upstream_varia = models.TextField(db_column='Gene_IL17B_interleukin_17B_minus_strand__2KB_Upstream_Varia', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_carmn_cardiac_mesoderm_enhancer_associated_non_coding_rna = models.TextField(db_column='Gene_CARMN_cardiac_mesoderm_enhancer_associated_non_coding_RNA', blank=True, null=True)  # Field name made lowercase.
    gene_pcyox1l_prenylcysteine_oxidase_1_like_plus_strand_500 = models.TextField(db_column='Gene_PCYOX1L_prenylcysteine_oxidase_1_like_plus_strand__500', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_loc101927046_uncharacterized_loc101927046_plus_strand_1 = models.TextField(db_column='Gene_LOC101927046_uncharacterized_LOC101927046_plus_strand_1', blank=True, null=True)  # Field name made lowercase.
    gene_carmn_cardiac_mesoderm_enhancer_associated_non_coding_rn2 = models.TextField(db_column='Gene_CARMN_cardiac_mesoderm_enhancer_associated_non_coding_RN2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'il17b'


class Il18(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il18_interleukin_18_minus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL18_interleukin_18_minus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_tex12_testis_expressed_12_plus_strand_2kb_upstream_va = models.TextField(db_column='Gene_TEX12_testis_expressed_12_plus_strand__2KB_Upstream_Va', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_loc107987164_uncharacterized_loc107987164_minus_strand = models.TextField(db_column='Gene_LOC107987164_uncharacterized_LOC107987164_minus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il18_interleukin_18_minus_strand = models.TextField(db_column='Gene_IL18_interleukin_18_minus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_il18_interleukin_18_minus_strand_500b_downstream_vari = models.TextField(db_column='Gene_IL18_interleukin_18_minus_strand__500B_Downstream_Vari', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_loc107987164_uncharacterized_loc107987164_minus_strand1 = models.TextField(db_column='Gene_LOC107987164_uncharacterized_LOC107987164_minus_strand1', blank=True, null=True)  # Field name made lowercase.
    gene_tex12_testis_expressed_12_plus_strand = models.TextField(db_column='Gene_TEX12_testis_expressed_12_plus_strand', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'il18'


class Il19(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il19_interleukin_19_plus_strand = models.TextField(db_column='Gene_IL19_interleukin_19_plus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_il10_interleukin_10_minus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL10_interleukin_10_minus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il10_interleukin_10_minus_strand = models.TextField(db_column='Gene_IL10_interleukin_10_minus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_loc105372878_uncharacterized_loc105372878_minus_strand = models.TextField(db_column='Gene_LOC105372878_uncharacterized_LOC105372878_minus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_il19_interleukin_19_plus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL19_interleukin_19_plus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_loc105372878_uncharacterized_loc105372878_minus_strand1 = models.TextField(db_column='Gene_LOC105372878_uncharacterized_LOC105372878_minus_strand1', blank=True, null=True)  # Field name made lowercase.
    gene_loc105372878_uncharacterized_loc105372878_minus_strand2 = models.TextField(db_column='Gene_LOC105372878_uncharacterized_LOC105372878_minus_strand2', blank=True, null=True)  # Field name made lowercase.
    gene_il19_interleukin_19_plus_strand_500b_downstream_varia = models.TextField(db_column='Gene_IL19_interleukin_19_plus_strand__500B_Downstream_Varia', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il19'


class Il1A(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il1a_interleukin_1_alpha_minus_strand = models.TextField(db_column='Gene_IL1A_interleukin_1_alpha_minus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il1a_interleukin_1_alpha_minus_strand_500b_downstream = models.TextField(db_column='Gene_IL1A_interleukin_1_alpha_minus_strand__500B_Downstream', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il1a_interleukin_1_alpha_minus_strand_2kb_upstream_va = models.TextField(db_column='Gene_IL1A_interleukin_1_alpha_minus_strand__2KB_Upstream_Va', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il1a'


class Il1B(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il1b_interleukin_1_beta_minus_strand = models.TextField(db_column='Gene_IL1B_interleukin_1_beta_minus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il1b_interleukin_1_beta_minus_strand_2kb_upstream_var = models.TextField(db_column='Gene_IL1B_interleukin_1_beta_minus_strand__2KB_Upstream_Var', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il1b_interleukin_1_beta_minus_strand_500b_downstream = models.TextField(db_column='Gene_IL1B_interleukin_1_beta_minus_strand__500B_Downstream', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il1b'


class Il2(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il2_interleukin_2_minus_strand = models.TextField(db_column='Gene_IL2_interleukin_2_minus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il2_interleukin_2_minus_strand_500b_downstream_varian = models.TextField(db_column='Gene_IL2_interleukin_2_minus_strand__500B_Downstream_Varian', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il2_interleukin_2_minus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL2_interleukin_2_minus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il2'


class Il20(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il20_interleukin_20_plus_strand = models.TextField(db_column='Gene_IL20_interleukin_20_plus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il20_interleukin_20_plus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL20_interleukin_20_plus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il20_interleukin_20_plus_strand_500b_downstream_varia = models.TextField(db_column='Gene_IL20_interleukin_20_plus_strand__500B_Downstream_Varia', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il20'


class Il21(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il21_interleukin_21_minus_strand = models.TextField(db_column='Gene_IL21_interleukin_21_minus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il21_as1_il21_antisense_rna_1_plus_strand = models.TextField(db_column='Gene_IL21_AS1_IL21_antisense_RNA_1_plus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_il21_interleukin_21_minus_strand_500b_downstream_vari = models.TextField(db_column='Gene_IL21_interleukin_21_minus_strand__500B_Downstream_Vari', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il21_as1_il21_antisense_rna_1_plus_strand_2kb_upstrea = models.TextField(db_column='Gene_IL21_AS1_IL21_antisense_RNA_1_plus_strand__2KB_Upstrea', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il21_interleukin_21_minus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL21_interleukin_21_minus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il21'


class Il22(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il22_interleukin_22_minus_strand = models.TextField(db_column='Gene_IL22_interleukin_22_minus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_loc105369818_uncharacterized_loc105369818_plus_strand = models.TextField(db_column='Gene_LOC105369818_uncharacterized_LOC105369818_plus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il22_interleukin_22_minus_strand_500b_downstream_vari = models.TextField(db_column='Gene_IL22_interleukin_22_minus_strand__500B_Downstream_Vari', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il22_interleukin_22_minus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL22_interleukin_22_minus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il22'


class Il23A(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il23a_interleukin_23_subunit_alpha_plus_strand = models.TextField(db_column='Gene_IL23A_interleukin_23_subunit_alpha_plus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_pan2_polya_specific_ribonuclease_subunit_pan2_minus_st = models.TextField(db_column='Gene_PAN2_polyA_specific_ribonuclease_subunit_PAN2_minus_st', blank=True, null=True)  # Field name made lowercase.
    gene_pan2_polya_specific_ribonuclease_subunit_pan2_minus_s1 = models.TextField(db_column='Gene_PAN2_polyA_specific_ribonuclease_subunit_PAN2_minus_s1', blank=True, null=True)  # Field name made lowercase.
    gene_il23a_interleukin_23_subunit_alpha_plus_strand_2kb_up = models.TextField(db_column='Gene_IL23A_interleukin_23_subunit_alpha_plus_strand__2KB_Up', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il23a_interleukin_23_subunit_alpha_plus_strand_500b_d = models.TextField(db_column='Gene_IL23A_interleukin_23_subunit_alpha_plus_strand__500B_D', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il23a'


class Il24(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il24_interleukin_24_plus_strand = models.TextField(db_column='Gene_IL24_interleukin_24_plus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il24_interleukin_24_plus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL24_interleukin_24_plus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_loc105372879_uncharacterized_loc105372879_minus_strand = models.TextField(db_column='Gene_LOC105372879_uncharacterized_LOC105372879_minus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_fcmr_fc_fragment_of_igm_receptor_minus_strand = models.TextField(db_column='Gene_FCMR_Fc_fragment_of_IgM_receptor_minus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_il24_interleukin_24_plus_strand_500b_downstream_varia = models.TextField(db_column='Gene_IL24_interleukin_24_plus_strand__500B_Downstream_Varia', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_fcmr_fc_fragment_of_igm_receptor_minus_strand_500b_do = models.TextField(db_column='Gene_FCMR_Fc_fragment_of_IgM_receptor_minus_strand__500B_Do', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_loc105372879_uncharacterized_loc105372879_minus_strand1 = models.TextField(db_column='Gene_LOC105372879_uncharacterized_LOC105372879_minus_strand1', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'il24'


class Il25(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_cmtm5_cklf_like_marvel_transmembrane_domain_containing_5 = models.TextField(db_column='Gene_CMTM5_CKLF_like_MARVEL_transmembrane_domain_containing_5', blank=True, null=True)  # Field name made lowercase.
    gene_il25_interleukin_25_plus_strand = models.TextField(db_column='Gene_IL25_interleukin_25_plus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il25_interleukin_25_plus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL25_interleukin_25_plus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_cmtm5_cklf_like_marvel_transmembrane_domain_containing_51 = models.TextField(db_column='Gene_CMTM5_CKLF_like_MARVEL_transmembrane_domain_containing_51', blank=True, null=True)  # Field name made lowercase.
    gene_il25_interleukin_25_plus_strand_500b_downstream_varia = models.TextField(db_column='Gene_IL25_interleukin_25_plus_strand__500B_Downstream_Varia', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il25'


class Il26(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il26_interleukin_26_minus_strand = models.TextField(db_column='Gene_IL26_interleukin_26_minus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_loc105369818_uncharacterized_loc105369818_plus_strand = models.TextField(db_column='Gene_LOC105369818_uncharacterized_LOC105369818_plus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il26_interleukin_26_minus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL26_interleukin_26_minus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il26_interleukin_26_minus_strand_500b_downstream_vari = models.TextField(db_column='Gene_IL26_interleukin_26_minus_strand__500B_Downstream_Vari', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    unnamed_0 = models.TextField(db_column='Unnamed_0', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'il26'


class Il27(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il27_interleukin_27_minus_strand = models.TextField(db_column='Gene_IL27_interleukin_27_minus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_apobr_apolipoprotein_b_receptor_plus_strand_500b_down = models.TextField(db_column='Gene_APOBR_apolipoprotein_B_receptor_plus_strand__500B_Down', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il27_interleukin_27_minus_strand_500b_downstream_vari = models.TextField(db_column='Gene_IL27_interleukin_27_minus_strand__500B_Downstream_Vari', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il27_interleukin_27_minus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL27_interleukin_27_minus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_apobr_apolipoprotein_b_receptor_plus_strand = models.TextField(db_column='Gene_APOBR_apolipoprotein_B_receptor_plus_strand', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'il27'


class Il3(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il3_interleukin_3_plus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL3_interleukin_3_plus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_loc105379174_uncharacterized_loc105379174_minus_strand = models.TextField(db_column='Gene_LOC105379174_uncharacterized_LOC105379174_minus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il3_interleukin_3_plus_strand = models.TextField(db_column='Gene_IL3_interleukin_3_plus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_loc105379174_uncharacterized_loc105379174_minus_strand1 = models.TextField(db_column='Gene_LOC105379174_uncharacterized_LOC105379174_minus_strand1', blank=True, null=True)  # Field name made lowercase.
    gene_il3_interleukin_3_plus_strand_500b_downstream_variant = models.TextField(db_column='Gene_IL3_interleukin_3_plus_strand__500B_Downstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il3'


class Il31(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_lrrc43_leucine_rich_repeat_containing_43_plus_strand = models.TextField(db_column='Gene_LRRC43_leucine_rich_repeat_containing_43_plus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_il31_interleukin_31_minus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL31_interleukin_31_minus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il31_interleukin_31_minus_strand = models.TextField(db_column='Gene_IL31_interleukin_31_minus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_il31_interleukin_31_minus_strand_500b_downstream_vari = models.TextField(db_column='Gene_IL31_interleukin_31_minus_strand__500B_Downstream_Vari', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il31'


class Il32(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il32_interleukin_32_plus_strand = models.TextField(db_column='Gene_IL32_interleukin_32_plus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il32_interleukin_32_plus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL32_interleukin_32_plus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il32_interleukin_32_plus_strand_500b_downstream_varia = models.TextField(db_column='Gene_IL32_interleukin_32_plus_strand__500B_Downstream_Varia', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il32'


class Il33(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il33_interleukin_33_plus_strand = models.TextField(db_column='Gene_IL33_interleukin_33_plus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_loc107987046_uncharacterized_loc107987046_minus_strand = models.TextField(db_column='Gene_LOC107987046_uncharacterized_LOC107987046_minus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il33_interleukin_33_plus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL33_interleukin_33_plus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_loc107987046_uncharacterized_loc107987046_minus_strand1 = models.TextField(db_column='Gene_LOC107987046_uncharacterized_LOC107987046_minus_strand1', blank=True, null=True)  # Field name made lowercase.
    gene_il33_interleukin_33_plus_strand_500b_downstream_varia = models.TextField(db_column='Gene_IL33_interleukin_33_plus_strand__500B_Downstream_Varia', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il33'


class Il34(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il34_interleukin_34_plus_strand = models.TextField(db_column='Gene_IL34_interleukin_34_plus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il34_interleukin_34_plus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL34_interleukin_34_plus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il34_interleukin_34_plus_strand_500b_downstream_varia = models.TextField(db_column='Gene_IL34_interleukin_34_plus_strand__500B_Downstream_Varia', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_mtss2_mtss_i_bar_domain_containing_2_minus_strand_500 = models.TextField(db_column='Gene_MTSS2_MTSS_I_BAR_domain_containing_2_minus_strand__500', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_sf3b3_splicing_factor_3b_subunit_3_plus_strand_500b_d = models.TextField(db_column='Gene_SF3B3_splicing_factor_3b_subunit_3_plus_strand__500B_D', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_mtss2_mtss_i_bar_domain_containing_2_minus_strand = models.TextField(db_column='Gene_MTSS2_MTSS_I_BAR_domain_containing_2_minus_strand', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'il34'


class Il36A(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il36a_interleukin_36_alpha_plus_strand = models.TextField(db_column='Gene_IL36A_interleukin_36_alpha_plus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il36a_interleukin_36_alpha_plus_strand_2kb_upstream_v = models.TextField(db_column='Gene_IL36A_interleukin_36_alpha_plus_strand__2KB_Upstream_V', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il36a_interleukin_36_alpha_plus_strand_500b_downstrea = models.TextField(db_column='Gene_IL36A_interleukin_36_alpha_plus_strand__500B_Downstrea', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il36a'


class Il36B(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il36b_interleukin_36_beta_minus_strand = models.TextField(db_column='Gene_IL36B_interleukin_36_beta_minus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il36b_interleukin_36_beta_minus_strand_2kb_upstream_v = models.TextField(db_column='Gene_IL36B_interleukin_36_beta_minus_strand__2KB_Upstream_V', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il36b_interleukin_36_beta_minus_strand_500b_downstrea = models.TextField(db_column='Gene_IL36B_interleukin_36_beta_minus_strand__500B_Downstrea', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il36b'


class Il37(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il37_interleukin_37_plus_strand = models.TextField(db_column='Gene_IL37_interleukin_37_plus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il37_interleukin_37_plus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL37_interleukin_37_plus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il37_interleukin_37_plus_strand_500b_downstream_varia = models.TextField(db_column='Gene_IL37_interleukin_37_plus_strand__500B_Downstream_Varia', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il37'


class Il4(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il4_interleukin_4_plus_strand = models.TextField(db_column='Gene_IL4_interleukin_4_plus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_loc105379176_uncharacterized_loc105379176_minus_strand = models.TextField(db_column='Gene_LOC105379176_uncharacterized_LOC105379176_minus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il4_interleukin_4_plus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL4_interleukin_4_plus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_loc105379176_uncharacterized_loc105379176_minus_strand1 = models.TextField(db_column='Gene_LOC105379176_uncharacterized_LOC105379176_minus_strand1', blank=True, null=True)  # Field name made lowercase.
    gene_il4_interleukin_4_plus_strand_500b_downstream_variant = models.TextField(db_column='Gene_IL4_interleukin_4_plus_strand__500B_Downstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_loc105379176_uncharacterized_loc105379176_minus_strand2 = models.TextField(db_column='Gene_LOC105379176_uncharacterized_LOC105379176_minus_strand2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'il4'


class Il5(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il5_interleukin_5_minus_strand = models.TextField(db_column='Gene_IL5_interleukin_5_minus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_rad50_rad50_double_strand_break_repair_protein_plus_stra = models.TextField(db_column='Gene_RAD50_RAD50_double_strand_break_repair_protein_plus_stra', blank=True, null=True)  # Field name made lowercase.
    gene_il5_interleukin_5_minus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL5_interleukin_5_minus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_rad50_rad50_double_strand_break_repair_protein_plus_str1 = models.TextField(db_column='Gene_RAD50_RAD50_double_strand_break_repair_protein_plus_str1', blank=True, null=True)  # Field name made lowercase.
    gene_il5_interleukin_5_minus_strand_500b_downstream_varian = models.TextField(db_column='Gene_IL5_interleukin_5_minus_strand__500B_Downstream_Varian', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il5'


class Il6(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il6_interleukin_6_plus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL6_interleukin_6_plus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il6_interleukin_6_plus_strand = models.TextField(db_column='Gene_IL6_interleukin_6_plus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_loc541472_uncharacterized_loc541472_minus_strand_2kb = models.TextField(db_column='Gene_LOC541472_uncharacterized_LOC541472_minus_strand__2KB', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_loc541472_uncharacterized_loc541472_minus_strand = models.TextField(db_column='Gene_LOC541472_uncharacterized_LOC541472_minus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_il6_interleukin_6_plus_strand_500b_downstream_variant = models.TextField(db_column='Gene_IL6_interleukin_6_plus_strand__500B_Downstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_loc541472_uncharacterized_loc541472_minus_strand_500b = models.TextField(db_column='Gene_LOC541472_uncharacterized_LOC541472_minus_strand__500B', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il6'


class Il7(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il7_interleukin_7_minus_strand = models.TextField(db_column='Gene_IL7_interleukin_7_minus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_loc105375914_uncharacterized_loc105375914_plus_strand = models.TextField(db_column='Gene_LOC105375914_uncharacterized_LOC105375914_plus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_zc2hc1a_zinc_finger_c2hc_type_containing_1a_plus_strand = models.TextField(db_column='Gene_ZC2HC1A_zinc_finger_C2HC_type_containing_1A_plus_strand', blank=True, null=True)  # Field name made lowercase.
    gene_zc2hc1a_zinc_finger_c2hc_type_containing_1a_plus_strand1 = models.TextField(db_column='Gene_ZC2HC1A_zinc_finger_C2HC_type_containing_1A_plus_strand1', blank=True, null=True)  # Field name made lowercase.
    gene_loc101241902_chromosome_4_open_reading_frame_46_pseudogen = models.TextField(db_column='Gene_LOC101241902_chromosome_4_open_reading_frame_46_pseudogen', blank=True, null=True)  # Field name made lowercase.
    gene_loc101241902_chromosome_4_open_reading_frame_46_pseudoge2 = models.TextField(db_column='Gene_LOC101241902_chromosome_4_open_reading_frame_46_pseudoge2', blank=True, null=True)  # Field name made lowercase.
    gene_il7_interleukin_7_minus_strand_500b_downstream_varian = models.TextField(db_column='Gene_IL7_interleukin_7_minus_strand__500B_Downstream_Varian', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il7_interleukin_7_minus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL7_interleukin_7_minus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_loc105375914_uncharacterized_loc105375914_plus_strand_field = models.TextField(db_column='Gene_LOC105375914_uncharacterized_LOC105375914_plus_strand_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    gene_loc101241902_chromosome_4_open_reading_frame_46_pseudoge3 = models.TextField(db_column='Gene_LOC101241902_chromosome_4_open_reading_frame_46_pseudoge3', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'il7'


class Il9(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    organism = models.TextField(db_column='Organism')  # Field name made lowercase.
    position = models.TextField(db_column='Postion')  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    variation_type = models.TextField(db_column='Variation_Type')  # Field name made lowercase.
    frequency = models.TextField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    clinical_significance = models.TextField(db_column='Clinical_Significance')  # Field name made lowercase.
    gene_consequence = models.TextField(db_column='Gene_Consequence')  # Field name made lowercase.
    publications = models.TextField(db_column='Publications', blank=True, null=True)  # Field name made lowercase.
    genomic_view = models.TextField(db_column='Genomic_View')  # Field name made lowercase.
    genomic_placements = models.TextField(db_column='Genomic_Placements')  # Field name made lowercase.
    gene_il9_interleukin_9_minus_strand = models.TextField(db_column='Gene_IL9_interleukin_9_minus_strand', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    gene_il9_interleukin_9_minus_strand_2kb_upstream_variant = models.TextField(db_column='Gene_IL9_interleukin_9_minus_strand__2KB_Upstream_Variant', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
    gene_il9_interleukin_9_minus_strand_500b_downstream_varian = models.TextField(db_column='Gene_IL9_interleukin_9_minus_strand__500B_Downstream_Varian', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.

    class Meta:
        managed = False
        db_table = 'il9'


class Main(models.Model):
    variant_id = models.CharField(db_column='Variant_ID', max_length=15, primary_key=True)  # Field name made lowercase.
    variant_type = models.CharField(db_column='Variant_Type', max_length=7)  # Field name made lowercase.
    alleles = models.TextField(db_column='Alleles')  # Field name made lowercase.
    chromosome = models.CharField(db_column='Chromosome', max_length=255)  # Field name made lowercase.
    gene = models.CharField(db_column='Gene', max_length=255)  # Field name made lowercase.
    functional_consequences = models.CharField(db_column='Functional_Consequences', max_length=255, blank=True, null=True)  # Field name made lowercase.
    validated = models.CharField(db_column='Validated', max_length=255, blank=True, null=True)  # Field name made lowercase.
    maf = models.TextField(db_column='MAF', blank=True, null=True)  # Field name made lowercase.
    hgvs = models.TextField(db_column='HGVS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'main'
