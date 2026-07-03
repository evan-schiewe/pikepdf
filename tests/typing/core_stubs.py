# SPDX-FileCopyrightText: 2026 James R. Barlow
# SPDX-License-Identifier: MPL-2.0

"""Static-only coverage for pikepdf core stubs."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

from pikepdf import (
    Array,
    AttachedFileSpec,
    Dictionary,
    Job,
    Matrix,
    Name,
    Object,
    Page,
    Pdf,
    Rectangle,
)


def _consume(*_values: object) -> None:
    pass


def _exercise_page_stubs(
    page: Page, formx: Object, name: Name, rect: Rectangle
) -> None:
    overlay_name: Name = page.add_overlay(page, shrink=False, expand=False)
    underlay_name: Name = page.add_underlay(page, shrink=False, expand=False)
    placement: bytes = page.calc_form_xobject_placement(formx, name, rect)

    resource: Object = page.form_xobjects[name]
    maybe_resource: Object | None = page.form_xobjects.get(name, default=None)
    page_index: int = page.index
    label: str = page.label

    page.emplace(page, retain=None)
    _consume(
        overlay_name,
        underlay_name,
        placement,
        resource,
        maybe_resource,
        page_index,
        label,
    )


def _exercise_object_stubs(obj: Object) -> None:
    values: Iterable[Object] = obj.values()
    obj.write(
        b"",
        filter=[Name.FlateDecode, Name.FlateDecode],
        decode_parms=[None, Dictionary()],
    )
    obj.emplace(obj, retain=None)
    _consume(values)


def _exercise_attachment_stubs(pdf: Pdf, path: Path) -> None:
    filespec = AttachedFileSpec(pdf, b"", relationship=Name.Data)
    filespec_from_path = AttachedFileSpec.from_filepath(
        pdf, path, relationship=Name.Data
    )
    _consume(filespec, filespec_from_path)


def _exercise_pdf_and_job_stubs(pdf: Pdf) -> None:
    with pdf.lock():
        pdf.flatten_annotations()

    json_schema: str = Job.json_out_schema()
    job_schema: str = Job.job_json_schema()
    _consume(json_schema, job_schema)


def _exercise_matrix_stubs(matrix: Matrix) -> None:
    from_array: Matrix = Matrix(Array([1, 0, 0, 1, 0, 0]))
    from_object_list: Matrix = Matrix(Array([1, 0, 0, 1, 0, 0]).as_list())
    latex: str = matrix._repr_latex_()
    truthy: bool = matrix.__bool__()
    _consume(from_array, from_object_list, latex, truthy)
