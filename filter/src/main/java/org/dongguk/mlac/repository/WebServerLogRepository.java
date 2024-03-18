package org.dongguk.mlac.repository;

import org.dongguk.mlac.domain.WebServerLog;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface WebServerLogRepository extends JpaRepository<WebServerLog, Long> {
}
