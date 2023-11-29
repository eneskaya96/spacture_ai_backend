from __future__ import annotations

import abc
import logging
from typing import Any

from src.domain.company.repositories import company_repository
from src.domain.face_detection.repositories import face_detection_repository
from src.domain.shoplifting.repositories import shoplifting_repository
from src.domain.watchlist.repositories import watchlist_repository, watchlist_face_detection_repository


class UnitOfWork(abc.ABC):
    logger = logging.getLogger(__name__)

    def __enter__(self) -> UnitOfWork:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        try:
            if not isinstance(exc_val, Exception):
                self.commit()
            else:
                self.rollback()
        except Exception as ex:
            self.logger.error('An error occurred performing a DB operation', exc_info=True)
            self.rollback()
            print('An error occurred performing a DB operation')

    @abc.abstractmethod
    def commit(self) -> None:
        pass

    @abc.abstractmethod
    def rollback(self) -> None:
        pass

    @abc.abstractmethod
    def is_in_context(self) -> bool:
        pass

    # region company Repositories
    @property
    @abc.abstractmethod
    def companies(self) -> company_repository.CompanyRepository:
        pass

    @property
    @abc.abstractmethod
    def face_detection(self) -> face_detection_repository.FaceDetectionRepository:
        pass

    @property
    @abc.abstractmethod
    def watchlist(self) -> watchlist_repository.WatchlistRepository:
        pass

    @property
    @abc.abstractmethod
    def watchlist_face_detection(self) -> watchlist_face_detection_repository.WatchlistFaceDetectionRepository:
        pass

    @property
    @abc.abstractmethod
    def shoplifting(self) -> shoplifting_repository.ShopliftingRepository:
        pass
    # endregion
