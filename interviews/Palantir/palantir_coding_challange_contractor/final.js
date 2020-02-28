class Entry {
    constructor(user, line_number, bound, version) {
        this.user = user
        this.line_number = line_number
        this.bound = bound
        this.version = version
    }

    set_task_id(id) {
        this.task_id = id
    }
}

class Solution {
    constructor(data_feed) {
        this.data_feed = data_feed
        this.version = 0
    }

    record_violation(entry, type) {
        let fraud = [entry.line_number, entry.user, type].join(';')
        this.res.push(fraud)
    }

    is_shortened_job(task_id, entry, should_record_violation = true) {
        let is_shortened = task_id < entry.bound

        if (is_shortened && should_record_violation) {
            this.record_violation(entry, 'SHORTENED_JOB')
        }

        if (!is_shortened) {
            this.min = Math.max(parseInt(task_id), this.min)
        }

        return is_shortened
    }

    find_violations() {
        this.res = []
        this.min = -Infinity

        this.entry_map = new Map()

        let line_number = 0;

        for (let line of this.data_feed) {
            line_number++

            let input = line.split(';')
            let user = input[0]

            if (input[1] === 'START') {
                this.entry_map[user] = this.entry_map[user] || []

                let entry = new Entry(user, line_number, this.min, this.version)
                this.entry_map[user].push(entry)
                continue;
            }

            // job completion
            this.version++
            let tasks = input[1].split(',')
            let is_batch = tasks.length > 1
            let contains_shortened_job = false

            let map = new Map()
            for (let index = 0; index < tasks.length; index++) {
                let entry = this.entry_map[user][index]
                let task_id = tasks[index]
                entry.set_task_id(task_id)
                let version = entry.version

                map[version] = map[version] || []
                map[version].push(entry)
            }

            for (let version in map) {
                let all_dirty = true;
                for (let entry of map[version]) {
                    if (this.is_shortened_job(entry.task_id, entry, false)) {
                        contains_shortened_job = true
                    } else {
                        all_dirty = false
                    }
                }

                if (all_dirty) {
                    for (let entry of map[version]) {
                        this.record_violation(entry, 'SHORTENED_JOB')
                    }
                }
            }

            // detect suspicious batch
            if (is_batch && contains_shortened_job) {
                this.record_violation(new Entry(user, line_number), 'SUSPICIOUS_BATCH')
            }

            delete this.entry_map[user]
        }

        return this.res
    }
}

function findViolations(datafeed) {
    return new Solution(datafeed).find_violations()
} 
